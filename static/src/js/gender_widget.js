odoo.define('gender_field_widget', function (require) {
"use strict";

var AbstractField = require('web.AbstractField');
var fieldRegistry = require('web.field_registry');

var genderField = AbstractField.extend({
    className: 'gender_field',
    tagName: 'span',
    events: {
        'click .GenderClass': 'ClickGender',
    },

    init: function () {
        this._super.apply(this, arguments);
    },

    _renderEdit: function () {
        this.$el.empty();
        var array = ['', 'Male', 'Female'];
        var selectList = document.createElement("select");
        selectList.className = "GenderClass";
        for (var i = 0; i < array.length; i++) {
            var option = document.createElement("option");
            option.value = array[i];
            option.text = array[i];
            selectList.appendChild(option);}

        this.$el.append(selectList);
    },

    _renderReadonly: function () {
        var className = "gender_" + this.value;
        this.$el.append($('<span>', {
            'class': className,
        }));
    },

    ClickGender: function (ev) {
        this._setValue(ev.currentTarget.value);

    }
});

fieldRegistry.add('gender_icon', genderField);

return {
    genderField: genderField,
};
});