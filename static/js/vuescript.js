 Vue.component('dynamic-option', {
            props: ['todo'],
            template: "<option :value='todo.text'>"
        })

         new Vue({
            el: '#container',
            data: {
                
                    checkedproducts: []
                  
            }
        })