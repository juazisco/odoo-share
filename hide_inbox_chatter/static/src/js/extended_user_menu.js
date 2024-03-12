/** @odoo-module **/
import { UserMenu } from "@web/webclient/user_menu/user_menu";
import { patch } from "@web/core/utils/patch";
import { registry } from "@web/core/registry";
const userMenuRegistry = registry.category("user_menuitems");


patch(UserMenu.prototype, {
    setup() {
        super.setup();
        userMenuRegistry.remove("documentation");
        userMenuRegistry.remove("support");
        userMenuRegistry.remove("odoo_account");
    },
    
});
