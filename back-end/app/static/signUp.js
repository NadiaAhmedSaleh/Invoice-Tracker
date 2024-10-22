
const userEmail=document.getElementById('email');
const signUpBtn=document.getElementById('signUpBtn');



//get email 
localStorage.setItem( "userEmail" , document.getElementById('email').value);

//save email to local storage
function saveToLocalStorage() {
    const inputValue = userEmail.value;
    localStorage.setItem('email', inputValue);
   
}
