# -*- coding: utf-8 -*-
{
    "name":
        "mana_dashboard",

    "summary":
        """
        Mana dashboard for odoo, advance dashboard for odoo, Bi builder for odoo. 
    """,
    
    "description":
        """
        mana dashboard for odoo,
        dashboard
        super dashboard
        advance dashboard
        advance dashboard for odoo
        dashboard for odoo
        odoo dashboard
        bi
        big data
        big data dashboard
        big data dashboard for odoo
        admin dashboard
        form builder
        reporter
        excel builder
        awesome odoo
        anita odoo
        editor
    """,
    "author":
        "Funenc Co., Ltd.",
    "website":
        "https://www.openerpnext.com",
    "live_test_url":
        "http://124.223.107.118:6010/web",
    "category":
        "application/dashboard",
    "version":
        "17.0.0.8",
    "price":
        10000,
    "currency":
        "EUR",
    "license":
        "OPL-1",
    "depends": [
        'base', 'mana_dashboard_base'
    ],
    "external_dependencies": {
        "python": ['json5', 'pendulum', 'python-box', 'xw_utils>=1.0.13']
    },
    "images": ['static/description/banner.png'],
    "data": [
        
        # security
        'security/ir.model.access.csv',
        'security/security.xml',
        
        # data
        'data/mana_series_type.xml',
        'data/mana_action_block_category.xml',
        'data/mana_aggregation_type.xml',
        'data/mana_field_datetime_range.xml',
        'data/mana_line_chart_template.xml',
        'data/mana_pie_chart_template.xml',

        # bar chart
        'data/bar_chart/simple_bar_chart.xml',
        'data/bar_chart/multi_group_bar_chart.xml',
        'data/bar_chart/radial_polar_bar_chart.xml',
        'data/bar_chart/tangential_polar_bar_chart.xml',
        'data/bar_chart/horizontal_bar_chart.xml',
        'data/mana_scatter_chart_template.xml',
        'data/mana_candlestick_chart_template.xml',
        'data/mana_radar_chart_template.xml',
        'data/mana_funnel_chart_template.xml',
        'data/mana_gauge_chart_template.xml',
        'data/mana_progress_bar_template.xml',
        'data/mana_percentage_template.xml',
        'data/mana_field_statistics.xml',
        'data/nama_search_group_sequence.xml',
        'data/mana_data_table.xml',
        'data/mana_sunburst_chart_template.xml',

        'data/mana_config_sequence.xml',
        'data/mana_timer_sequence.xml',

        # assets
        'data/mana_assets_sub_type.xml',
        'data/mana_assets_type.xml',
        'data/mana_assets_bk.xml',
        'data/mana_assets_title.xml',
        'data/mana_assets_border.xml',

        'data/mana_custom_chart_template.xml',
        'data/mana_none_template.xml',
        
        # views
        'views/mana_dashboard.xml',
        'views/mana_group_by_info.xml',
        'views/mana_aggregation_type.xml',
        'views/mana_template.xml',
        'views/mana_send_to_dashboard.xml',
        'views/mana_action_blocks.xml',
        'views/mana_dashboard_template.xml',
        'views/mana_template.xml',
        'views/mana_history_data.xml',
        'views/mana_order_by_info.xml',
        'views/mana_template_base.xml',
        'views/mana_field_info.xml',
        'views/mana_raw_field_info.xml',
        'views/mana_config.xml',
        'views/mana_content_editor.xml',
        'views/mana_datetime_range.xml',
        'views/mana_range_filter_traits.xml',
        'views/mana_search_info.xml',
        'views/mana_bind_menu_wizard.xml',
        'views/mana_data_source.xml',
        'views/mana_marquee_traits.xml',
        'views/mana_dashboard_import_wizard.xml',
        'views/mana_any_config.xml',
        'views/mana_timer_config.xml',
        'views/mana_search_group_traits.xml',
        'views/mana_dashboard_parameter.xml',
        'views/mana_dashboard_series_type.xml',
        'views/mana_dashboard_template.xml',
        'views/mana_dashboard_block_settings.xml',
        'views/mana_assets_sub_type.xml',
        'views/mana_dashboard_actions.xml',
        'views/mana_assets.xml',
        'views/mana_assets_type.xml'
    ],
    'assets': {
        'web.assets_backend': [

            # css
            "/mana_dashboard/static/css/mana_dashboard.scss",
            "/mana_dashboard/static/css/layout.scss",
            "/mana_dashboard/static/css/search.scss",
            "/mana_dashboard/static/libs/style_bg/grapick.css",

            # libs
            "/mana_dashboard/static/libs/color_picker/color_picker.js",
            "/mana_dashboard/static/libs/tabulator/css/tabulator.min.css",
            "/mana_dashboard/static/libs/tabulator/css/tabulator_bootstrap4.css",

            # tabulator
            "/mana_dashboard/static/libs/tabulator/js/tabulator.min.js",
            "/mana_dashboard/static/libs/bootstrap_blocks/blocks.min.js",

            # style_bg
            "/mana_dashboard/static/libs/style_bg/grapesjs-style-bg.min.js",

            # dialog
            "/mana_dashboard/static/src/dialog/mana_dialog.js",
            "/mana_dashboard/static/src/dialog/mana_dialog.xml",

            # dashboard
            "/mana_dashboard/static/src/color_picker/color_picker.js",
            "/mana_dashboard/static/src/color_picker/color_picker.scss",
            "/mana_dashboard/static/src/color_picker/color_picker.xml",

            # color picker list
            "/mana_dashboard/static/src/color_picker_list/color_picker_list.js",
            "/mana_dashboard/static/src/color_picker_list/color_picker_list.xml",

            # according
            "/mana_dashboard/static/src/mana_accordion/mana_accordion.js",
            "/mana_dashboard/static/src/mana_accordion/mana_accordion.xml",
            "/mana_dashboard/static/src/mana_accordion/mana_accordion.scss",

            # config number
            "/mana_dashboard/static/src/mana_config_number/mana_config_number.js",
            "/mana_dashboard/static/src/mana_config_number/mana_config_number.xml",

            # config color
            "/mana_dashboard/static/src/mana_config_color/mana_config_color.js",
            "/mana_dashboard/static/src/mana_config_color/mana_config_color.xml",

            # color list config
            "/mana_dashboard/static/src/mana_config_color_list/mana_config_color_list.js",
            "/mana_dashboard/static/src/mana_config_color_list/mana_config_color_list.xml",

            # theme builder css
            "/mana_dashboard/static/src/theme_builder/css/_configs.color.scss",
            "/mana_dashboard/static/src/theme_builder/css/_settings.global.scss",
            "/mana_dashboard/static/src/theme_builder/css/_components.echarts.scss",
            "/mana_dashboard/static/src/theme_builder/css/_components.config.scss",
            "/mana_dashboard/static/src/theme_builder/css/_components.color.scss",
            "/mana_dashboard/static/src/theme_builder/css/_components.code.scss",

            # theme builder
            "/mana_dashboard/static/src/theme_builder/theme_builder.js",
            "/mana_dashboard/static/src/theme_builder/theme_builder.xml",

            # color picker list
            "/mana_dashboard/static/src/color_picker_list/color_picker_list.js",
            "/mana_dashboard/static/src/color_picker_list/color_picker_list.xml",

            # json editor
            "/mana_dashboard/static/src/json_editor/json_editor.js",
            "/mana_dashboard/static/src/json_editor/json_editor.xml",

            # preset
            "/mana_dashboard/static/src/editor_preset/editor_preset.js",

            # spectrum
            "/mana_dashboard/static/libs/spectrum/spectrum.js",
            "/mana_dashboard/static/libs/spectrum/spectrum.css",

            # charts
            "/mana_dashboard/static/src/charts/mana_pie_chart.js",
            "/mana_dashboard/static/src/charts/mana_bar_chart.js",
            "/mana_dashboard/static/src/charts/mana_line_chart.js",
            "/mana_dashboard/static/src/charts/mana_radar_chart.js",
            "/mana_dashboard/static/src/charts/mana_funnel_chart.js",
            "/mana_dashboard/static/src/charts/mana_gauge_chart.js",
            "/mana_dashboard/static/src/charts/mana_custom_chart.js",
            "/mana_dashboard/static/src/charts/mana_scatter_chart.js",
            "/mana_dashboard/static/src/charts/mana_candlestick.js",
            "/mana_dashboard/static/src/charts/mana_sunburst_chart.js",

            # preview_widget
            "/mana_dashboard/static/src/preview_widget/preview_widget.js",
            "/mana_dashboard/static/src/preview_widget/preview_widget.xml",

            # basic blocks
            "/mana_dashboard/static/src/basic_blocks/mana_basic_blocks.js",

            # action widget
            "/mana_dashboard/static/src/action_widget/mana_action_block.js",

            # percentage
            "/mana_dashboard/static/src/percentage_block/percentage_block.js",

            # field_statistics
            "/mana_dashboard/static/src/field_statistics/field_statistics.js",

            # progress
            "/mana_dashboard/static/src/progress_bar/progress_bar.js",

            # hls video
            "/mana_dashboard/static/src/hls_video/hls_video.js",

            # svg block
            "/mana_dashboard/static/src/svg_block/svg_block.js",

            # date filter
            "/mana_dashboard/static/src/utils/mana_date_util.js",

            # add to dashboard
            "/mana_dashboard/static/src/send_to_dashboard/send_to_dashboard.js",

            # content
            "/mana_dashboard/static/src/content_block/content_block.js",

            # mana sub form view
            "/mana_dashboard/static/src/sub_form_view/mana_sub_form.js",
            "/mana_dashboard/static/src/sub_form_view/mana_sub_form.xml",
            "/mana_dashboard/static/src/sub_form_view/mana_view.js",

            # chart traits
            "/mana_dashboard/static/src/trait/form_trait.js",
            "/mana_dashboard/static/src/trait/option_trait.js",
            "/mana_dashboard/static/src/trait/many2one_trait.js",

            # iframe
            "/mana_dashboard/static/src/iframe_widget/iframe_widget.js",

            # data table
            "/mana_dashboard/static/src/data_table/data_table.js",

            # grid widget
            "/mana_dashboard/static/src/grid_widget/grid_widget.js",

            # layout
            "/mana_dashboard/static/src/layout/flex_row.js",
            "/mana_dashboard/static/src/layout/flex_column.js",

            # daterangepicker
            "/mana_dashboard/static/libs/daterangepicker/daterangepicker.js",
            "/mana_dashboard/static/libs/daterangepicker/daterangepicker.css",

            # mutex_toggle
            "/mana_dashboard/static/src/mutex_toggle/mutex_toggle.js",

            # fake_field
            "/mana_dashboard/static/src/fake_field/fake_field.js",

            # dashboard
            "/mana_dashboard/static/src/mana_dashboard.js",
            "/mana_dashboard/static/src/mana_dashboard.xml",

            # mana_form_controller
            "/mana_dashboard/static/src/mana_form_controller.js",

            # mana_relation_utils
            "/mana_dashboard/static/src/mana_relation_utils.js",

            # preview_many2one
            "/mana_dashboard/static/src/preview_many2one/*.*",

            # misc
            "/mana_dashboard/static/xml/misc.xml"
        ]
    }
}
