document.addEventListener('DOMContentLoaded', () => {

});

function getVariants(){
  fetch('/products/variants')
  .then(response => response.json())
  .then(data => {
    console.log(data);
  }).catch(err => {
    console.log('Error getting variants: ', err);
  });
}