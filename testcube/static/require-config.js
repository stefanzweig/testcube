requirejs.config({
    baseUrl: '/static/libs',
    shim: {
        'bootstrap': {
            deps: ['jquery', 'bootstrap_fix'],
            exports: '$.fn.popover'
        },
        bootstrapTable: {
            deps: ['bootstrap'],
            exports: '$.fn.bootstrapTable'
        },
        bootstrapSelect: {
            deps: ['bootstrap'],
            exports: '$.fn.selectpicker'
        },
        bootstrapTagsInput: {
            deps: ['bootstrap'],
            exports: '$.fn.tagsinput'
        },
        'bootstrap-dialog': {
            deps: ['bootstrap']
        },
        'lightbox': {
            deps: ['jquery'],
            exports: '$.fn.ekkoLightbox'
        },
        bootstrapTableCookie: {
            deps: ['bootstrapTable'],
            exports: '$.fn.bootstrapTable.defaults'
        },
        typeahead: {
            deps: ['jquery'],
            init: function ($) {
                return require.s.contexts._.registry['typeahead.js'].factory($);
            }
        },
        bloodhound: {
            deps: ['jquery'],
            exports: 'Bloodhound'
        },
        rainbow: {
            exports: 'Rainbow'
        },
        rainbow_generic: {
            deps: ['rainbow']
        },
        rainbow_python: {
            deps: ['rainbow_generic']
        },
        rainbow_log: {
            deps: ['rainbow_python']
        }
    },
    paths: {
        bootstrap: 'bootstrap/js/bootstrap.min',
        bootstrap_fix: 'bootstrap/js/ie10-viewport-bug-workaround',
        bootstrapTable: 'bootstrap-table/bootstrap-table.min',
        bootstrapSelect: 'bootstrap-select/bootstrap-select.min',
        bootstrapTagsInput: 'bootstrap-tagsinput/bootstrap-tagsinput.min',
        bootstrapCookie: 'bootstrap-table/bootstrap-table-cookie',
        bootstrapTypeAhead: 'bootstrap-typeahead/bootstrap3-typeahead.min',
        'bootstrap-dialog': 'bootstrap-dialog/bootstrap-dialog.min',
        c3: 'c3.min',
        d3: 'd3.min',
        jquery: 'jquery-3.2.1.min',
        'js-cookie': 'js.cookie-2.1.4',
        lodash: 'lodash.min',
        marked: 'marked.min',
        moment: 'moment.min',
        mustache: 'mustache.min',
        common: '../common',
        'table-config': '../table-config',
        'table-func': '../table-func',
        signup: '../signup',
        'chart-func': '../chart-func',
        rainbow: 'rainbow/rainbow',
        rainbow_generic: 'rainbow/language/generic',
        rainbow_python: 'rainbow/language/python',
        rainbow_log: 'rainbow/language/log',
        typeahead: 'typeaheadjs/typeahead.jquery',
        bloodhound: 'typeaheadjs/bloodhound',
        'case-detail': '../case-detail',
        'lightbox': 'ekko-lightbox/ekko-lightbox'
    },
    deps: ['bootstrap']
});

window.app = {};

if (!window.localStorage) {
    window.localStorage = {};
}

window.waitForLoading = function () {
    require(['jquery'], function ($) {
        $('#loading-icon').removeClass('hidden');
    })
};

window.loadingCompleted = function () {
    require(['jquery'], function ($) {
        $('#loading-icon').addClass('hidden');
    })
};

