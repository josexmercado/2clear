 Vue.component('dynamic-option', {
            props: ['todo'],
            template: "<option :value='todo.text'>"
        })

        var autoCompleteSearchApp = new Vue({
            el: '#home',
            data: {
                add: 'Add Customer',
                view: 'View Customer Records',
                custname: 'Customer Name: ',
            }
        })