---
title: "OCA加密存储外部账号密码keychain"
source: "http://www.thinkltd.cn/forum/2/ocakeychain-2760"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# OCA加密存储外部账号密码keychain

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/ocakeychain-2760>

模块链接：

This module allows you to store credentials of external systems.

- All the crendentials are stored in one place: easier to manage and to audit.
- Multi-account made possible without effort.
- Store additionnal data for each account.
- Validation rules for additional data.
- Have different account for different environments (prod / test / env / etc).

By default, passwords are encrypted with a key stored in Odoo config. It's far from an ideal password storage setup, but it's way better than password in clear text in the database. It can be easily replaced by another system. See "Security" chapter below.

Accounts may be: market places (Amazon, Cdiscount, ...), carriers (Laposte, UPS, ...) or any third party system called from Odoo.

This module is aimed for developers. The logic to choose between accounts will be achieved in dependent modules.

##

## Uses cases

Possible use case for deliveries: you need multiple accounts for the same carrier. It can be for instance due to carrier restrictions (immutable sender address), or business rules (each warehouse use a different account).

###

### Configuration

After the installation of this module, you need to add some entries in Odoo's config file: (etc/openerp.cfg)

> keychain_key = fyeMIx9XVPBBky5XZeLDxVc9dFKy7Uzas3AoyMarHPA=

You can generate keys with python -c 'from cryptography.fernet import Fernet; print Fernet.generate_key()'.

This key is used to encrypt account passwords.

If you plan to use environments, you should add a key per environment:

> keychain_key_dev = 8H_qFvwhxv6EeO9bZ8ww7BUymNt3xtQKYEq9rjAPtrc=

> keychain_key_prod = y5z-ETtXkVI_ADoFEZ5CHLvrNjwOPxsx-htSVbDbmRc=

keychain_key is used for encryption when no environment is set.

###

### Usage (for module dev)

- Add this keychain as a dependency in __manifest__.py
- Subclass keychain.account and add your module in namespaces: (see after for the name of namespace )

```python
    class LaposteAccount(models.Model):
        _inherit = 'keychain.account'
        namespace = fields.Selection(
            selection_add=[('roulier_laposte', 'Laposte')])
```

- Add the default data (as dict):

    class LaposteAccount(models.Model):
        # ...
```python
        def _roulier_laposte_init_data(self):
            return {
                "agencyCode": "",
                "recommandationLevel": "R1"
            }
```

- Implement validation of user entered data:

    class LaposteAccount(models.Model):
        # ...
        def _roulier_laposte_validate_data(self, data):
            return len(data.get("agencyCode") > 3)

- In your code, fetch the account:

```python
    import random
    def _get_auth(self):
        keychain = self.env['keychain.account']
        if self.env.user.has_group('stock.group_stock_user'):
            retrieve = keychain.suspend_security().retrieve
        else:
            retrieve = keychain.retrieve
        accounts = retrieve(
```

            [['namespace', '=', 'roulier_laposte']])
```python
        account = random.choice(accounts)
        return {
            'login': account.login,
            'password': account.get_password()
        }
```

In this example, an account is randomly picked. Usually this is set according to rules specific for each client.

You have to restrict user access of your methods with suspend_security().

Warning: _init_data and _validate_data should be prefixed with your namespace! Choose python naming function compatible name.

###

### Switching from prod to dev

You may adopt one of the following strategies:

- store your dev accounts in production db using the dev key
- import your dev accounts with Odoo builtin methods like a data.xml (in a dedicated module).
- import your dev accounts with your own migration/cleanup script
- etc.

Note: only the password field is unreadable without the proper key, login and data fields are available on all environments.

You may also use a same technical_name and different environment for choosing at runtime between accounts.

###

### Usage (for user)

Go to *settings / keychain*, create a record with the following

- Namespace: type of account (ie: Laposte)
- Name: human readable label "Warehouse 1"
- Technical Name: name used by a consumer module (like "warehouse_1")
- Login: login of the account
- Password_clear: For entering the password in clear text (not stored unencrypted)
- Password: password encrypted, unreadable without the key (in config)
- Data: a JSON string for additionnal values (additionnal config for the account, like: {"agencyCode": "Lyon", "insuranceLevel": "R1"})
- Environment: usually prod or dev or blank (for all)

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
