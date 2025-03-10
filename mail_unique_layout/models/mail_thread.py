# Copyright 2021 Akretion
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, models


class MailThread(models.AbstractModel):
    _inherit = "mail.thread"

    @api.model
    def _get_default_unique_layout_ref(self):
        return "mail_unique_layout.general_mail_layout"

    @api.model
    def _get_unique_layout_ref(self):
        if self._context.get("force_mail_uniq_layout_id"):
            return self._context["force_mail_uniq_layout_id"]
        else:
            return self._get_default_unique_layout_ref()

    @api.returns("mail.message", lambda value: value.id)
    def message_post(self, *kw, **kwargs):
        kwargs["email_layout_xmlid"] = self._get_unique_layout_ref()
        return super().message_post(*kw, **kwargs)
