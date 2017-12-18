

  var customerlist=new Vue({
  el: '#customerlist',
  data: {
    messages: ['value1', 'value2', 'value3','value4'],
    selected: ''
    },
  methods: {
  	onSelect: function(msg) {
    	this.selected = msg
    }
  }
})
var addcontent =new Vue({
  el: '#addcontent',
  data: {
    add: 'Add Customer',
    view: 'View Customer Records'
  }
})
