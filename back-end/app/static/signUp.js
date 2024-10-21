//front validation

const fullName=document.getElementById('fullName');
const userName=document.getElementById('userName');
const userEmail=document.getElementById('email');
const password=document.getElementById('password');
const repassword=document.getElementById('repassword');
const signUpBtn=document.getElementById('signUpBtn');

const errorText=document.getElementById("nameError");


//get email 
localStorage.setItem( "userEmail" , document.getElementById('email').value);

//save email to local storage
function saveToLocalStorage() {
    const inputValue = userEmail.value;
    localStorage.setItem('email', inputValue);
    alert('Saved!');
}


//sign up form validation

//fullname validation

function validateName(){
    if (fullName.value.length > 10 || fullName.value.length == " ") 
    {
        errorText.textContent = "Only 10 letters are allowed!";
        signUpBtn.setAttribute('disabled')
    }
}

validateName();

//email validation

function validateUserName(){
    if (userName.value.length > 10 || userName.value.length == "") 
    {
        errorText.textContent = "Only 10 letters are allowed!";
        signUpBtn.setAttribute('disabled')
    }
}



//username validation

function validateUserName(){
    if (userName.value.length > 10 || userName.value.length == "") 
    {
        errorText.textContent = "Only 10 letters are allowed!";
        signUpBtn.setAttribute('disabled')
    }
}

//hellloooo


//email validation

userEmail.onkeyup=function emailValidation(){
    userEmail.value;
    let emailRegex=/^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    let valresult=emailRegex.test(userEmail.value);

    if(valresult==false){
        document.getElementById("emailError").textContent="email should be ahmedxyz@gmail.com";

    }
    return true;
 }