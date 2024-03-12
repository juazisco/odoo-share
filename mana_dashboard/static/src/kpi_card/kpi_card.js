/** @odoo-module alias=mana_dashboard.gauge_chart **/
/** @odoo-module alias=mana_dashboard.gauge_chart **/

import { BlockRegistry } from '@mana_dashboard_base/mana_block_registry';
import { icons } from "@mana_dashboard_base/utils/mana_icons";
import { QWebBlock } from "@mana_dashboard_base/qweb_block/qweb_block";

const QWebBlockModel = QWebBlock.QWebBlockModel;
const QWebBlockView = QWebBlock.QWebBlockView;

import { icons } from "@mana_dashboard_base/utils/mana_icons";
import { _t } from "@web/core/l10n/translation";


function builder(editor, options) {

    const dc = editor.DomComponents;

    /**
     * kpi card
     */
    editor.BlockManager.add('kpi_card', {
        label: _t('Kpi Card'),
        category: _t('Statistics'),
        select: true,

        render: () => {
            return `<div class="d-flex flex-column align-items-center justify-content-center"><div class="chart-icon-custom">${icons.kpi_card}</div><div class='anita-block-label'>Kpi Card</div></div>`
        },

        content: {
            type: 'kpi_card',
        }
    });

    /**
     * Progress Bar
     */
    dc.addType('kpi_card', {

        model: QWebBlockModel.extend({
            defaults: {
                ...QWebBlockModel.prototype.defaults,

                name: _t('Kpi Card'),
                classes: ['kpi_card'],
                attributes: {},

                default_template: 'mana_dashboard.kpi_card_style_one',
                template_category: 'statistics',
                template_type: 'kpi_card',
                search_sensitive: true,
                auto_load_config: true,
                disable_children: false,
                disable_first_child: true,
                dynamic_default_template: true,
            },

            initialize() {
                QWebBlockModel.prototype.initialize.apply(this, arguments);
            }
        }, {
            isComponent: (el) => {
                if (el && el.classList && el.classList.contains('kpi_card')) {
                    return {
                        type: 'kpi_card',
                    };
                }
            }
        }),

        view: QWebBlockView.extend({
            init() {
                QWebBlockView.prototype.init.apply(this, arguments);
            },
        })
    });
}
