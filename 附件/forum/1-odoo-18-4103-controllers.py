from odoo import http
from odoo.http import request
import requests
import json
import logging
import pytz

_logger = logging.getLogger(__name__)
"""

2025.02.07 手机号更新路逻辑：
1.进入登录页面，直接创建用户
2.查询是否有手机号，如果没有手机号，需要更新
3.如果有手机号，可以更新手机号

"""


class WeChatLoginController(http.Controller):
    @http.route('/mini/wechat_login', type='json', auth='public', csrf=False, methods=['POST'])
    def wechat_login(self, **kwargs):
        try:
            json_data = json.loads(request.httprequest.data)
            if not json_data:
                return {'success': False, 'message': '请求参数错误'}

            code = json_data.get('code')
            if not code:
                return {'success': False, 'message': '缺少微信登录 code'}

            # 获取微信配置
            configs = request.env['ir.config_parameter'].sudo()
            app_id = configs.get_param('wechat_mini_app_id')
            app_secret = configs.get_param('wechat_mini_app_secret')
            wechat_login_url = configs.get_param('wechat_mini_login_url')

            if not all([app_id, app_secret, wechat_login_url]):
                return {'success': False, 'message': '未正确配置微信登录参数'}

            # 调用微信登录接口
            url = f"{wechat_login_url}?appid={app_id}&secret={app_secret}&js_code={code}&grant_type=authorization_code"
            response = requests.get(url)
            response.raise_for_status()

            session_data = response.json()
            print(session_data, '返回的数据是')
            if 'errcode' in session_data:
                return {'success': False, 'message': session_data.get('errmsg', '微信认证失败')}

            openid = session_data.get('openid')
            unionid = session_data.get('unionid')
            session_key = session_data.get('session_key')

            if not openid or not session_key:
                return {'success': False, 'message': '微信登录失败，缺少必要的用户信息'}

            user = False

            if openid:
                user = request.env['res.users'].sudo().search([('wechat_mini_openid', '=', openid)], limit=1)

            if not user:
                return {'success': False, 'message': '没有维护 研易云系统用户账号'}
                # user_data = {
                #     'name': f'微信用户_{unionid[-6:]}' if unionid else f'微信用户_{openid[-6:]}',
                #     'login': unionid or openid,
                #     'wechat_mini_openid': openid,
                #     'wechat_unionid': unionid
                # }
                # user = request.env['res.users'].sudo().create(user_data)


            # 手动登录用户
            request.session.uid = user.id
            request.session.login = user.login
            request.session.session_token = user._compute_session_token(request.session.sid)
            try:
                user = user.with_user(user)
                tz = request.httprequest.cookies.get('tz') if request else None
                if tz in pytz.all_timezones and (not user.tz or not user.login_date):
                    # first login or missing tz -> set tz to browser tz
                    user.tz = tz
                user._update_last_login()
            except Exception as e:
                _logger.error(f"WeChat login error: {e}")

            configs = request.env['ir.config_parameter'].sudo()
            if len(user.employee_ids) == 1:
                employee_id = user.employee_id.id
            elif len(user.employee_ids) > 1:
                employee_id = user.employee_ids[0].id
            else:
                employee_id = False
            # 返回成功响应
            return {
                'success': True,
                'message': '登录成功',
                'user_info': {
                    'employee_id': employee_id,
                    'info_id': user.id,
                    # 'open_id': user.wechat_mini_openid,
                    # 'unionid': user.wechat_unionid,
                    # 'name': user.name,
                    'token': request.session.sid,  # 返回 session ID
                    'login': user.login
                }
            }
        except Exception as e:
            _logger.error(f"WeChat login error: {e}")
            return {'success': False, 'message': '服务器内部错误'}




    @http.route('/mini/get_user_phone', type='json', auth='none', csrf=False, methods=['POST'])
    def get_user_phone(self, **kwargs):
        try:
            # print(kwargs)
            json_data = kwargs
            if not json_data:
                return {'success': False, 'message': '请求参数错误'}

            code = json_data.get('code')
            openid = json_data.get('openid')
            unionid = json_data.get('unionid')

            if not openid and not unionid:
                return {'success': False, 'message': '请提供对应的用户数据'}

            user = False

            if openid:
                user = request.env['res.users'].sudo().search([('wechat_mini_openid', '=', openid)], limit=1)

            if unionid:
                user = request.env['res.users'].sudo().search([('wechat_unionid', '=', unionid)], limit=1)

            if not code:
                return {'success': False, 'message': '缺少微信登录 code'}
            # 获取微信配置
            configs = request.env['ir.config_parameter'].sudo()
            app_id = configs.get_param('wechat_mini_app_id')
            app_secret = configs.get_param('wechat_mini_app_secret')

            access_token_url = f'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={app_id}&secret={app_secret}'
            token_response = requests.get(access_token_url)
            if token_response.status_code != 200:
                return {'success': False, 'message': '获取微信 access_token 失败'}

            token_response_data = token_response.json()
            access_token = token_response_data.get('access_token')
            # 调用微信登录接口
            url = f"https://api.weixin.qq.com/wxa/business/getuserphonenumber?access_token={access_token}"
            data_body = {
                "code": code  # 替换为实际的 code

            }
            headers = {
                'Content-Type': 'application/json'
            }
            phone_response = requests.post(url, json=data_body, headers=headers)
            if phone_response.status_code != 200:
                return {'success': False, 'message': '获取手机号响应异常'}
            phone_response_data = phone_response.json()
            # print(phone_response_data, '返回数据')
            if phone_response_data.get('errcode') == 0:
                phone_info = phone_response_data.get('phone_info')
                phone_no = phone_info.get('phoneNumber')

                if user:
                    phone_no_to_add = phone_no.strip()  # 确保新添加的电话号码没有多余的空格

                    # 初始化phone_nos列表
                    phone_nos_list = [pn.strip() for pn in user.phone_nos.split(',')] if user.phone_nos else []

                    # 如果phone_no_to_add不在phone_nos_list中，则添加
                    if phone_no_to_add not in phone_nos_list:
                        phone_nos_list.append(phone_no_to_add)

                    # 将列表重新组合成字符串并更新user.phone_nos
                    all_phone_nos = ','.join(phone_nos_list)
                    user.write({
                        'phone_no': phone_no,
                        'phone_nos': all_phone_nos
                    })

                return {'success': True, 'message': '获取手机号成功', 'phone_no': phone_no}
            else:

                return {'success': False, 'message': '获取手机号失败'}
        except Exception as e:
            _logger.error(f"获取手机号失败: {e}")
            return {'success': False, 'message': '获取手机号失败,报错'}
