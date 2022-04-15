document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll(".btnVariant").forEach(btn => {
    btn.addEventListener('click', () => {
      let btnVariant= event.currentTarget;
      addToCart(btn, product, btnVariant.dataset.variant_id, 'http://localhost:8000/cart/')
    });
  });
});

function addToCart(btn, productId, variantId, url){
  let stockElement= document.getElementById('stock_'+variantId);
  let stock= stockElement.textContent.match(/\d+/);
  if(stock > 1){
    stock -= 1;
    stockElement.textContent= "Stock: " + stock; 
  }else if (stock == 1){
    stock -= 1;
    stockElement.textContent= "Stock: " + stock; 
    btn.disabled= true;
    btn.textContent= "There is no stock";
  }
  data= {
    product_id: productId,
    variant_id: variantId
  }
  fetch(url, {
    method: 'POST',
    mode: 'cors',
    body: JSON.stringify(data)
  }).then(response => response.json())
  .then(data => {
    console.log(data);
  }).catch(err => {
    console.log('Error adding to cart: ', err);
  });
}