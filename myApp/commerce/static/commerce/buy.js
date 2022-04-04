document.addEventListener('DOMContentLoaded', () => {
  getPayMethods('http://localhost:8000/pay_methods/');
  document.querySelector('form').addEventListener('submit', () => {
    event.preventDefault();
    let form= event.currentTarget;
    goToBuy('http://localhost:8000/buy/', document.querySelector('input[name="radios_options"]:checked').value, form['address'].value);
  });
});

function getPayMethods(url){
  fetch(url)
  .then(response => response.json())
  .then(data => {
    let a= 0;
    data.forEach(pay_method => {
      let div= document.createElement('div');
      div.className= 'form-check';
      let radio_o= document.createElement('input');
      radio_o.type= 'radio';
      radio_o.setAttribute('id', 'radio_'+a);
      radio_o.value= pay_method.pay_method;
      radio_o.name= 'radios_options';
      radio_o.required= true;
      a++;
      radio_o.className= 'form-check-input';
      let radio_l= document.createElement('label');
      radio_l.className= 'form-check-label';
      radio_l.setAttribute('for', radio_o.getAttribute('id'));
      radio_l.textContent= pay_method.pay_method;
      div.appendChild(radio_o);
      div.appendChild(radio_l);
      document.querySelector('form').prepend(div);
    });
  }).catch(err => {
    console.log('Error getting pay methods: ', err);
  });
}

function goToBuy(url, pay_method, address){
  console.log(pay_method, address);
  data= {
    pay_method: pay_method,
    address: address
  }
  fetch(url, {
    method: 'POST',
    mode: 'cors',
    body: JSON.stringify(data)
  }).then(response => response.json())
  .then(data => {
    console.log(data);
  }).catch(err => {
    console.log('Error while trying to go to the buy form: ', err);
  });
}