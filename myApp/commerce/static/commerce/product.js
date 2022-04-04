document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll(".btnVariant").forEach(btn => {
    btn.addEventListener('click', () => {
      let btnVariant= event.currentTarget;
      console.log(product);
      addToCart(product, btnVariant.dataset.variant_id, 'http://localhost:8000/cart/')
    });
  });
});

function addToCart(productId, variantId, url){
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