//front validation
let fullName=document.getElementById('fullName');
let userName=document.getElementById('userName');
let userEmail=document.getElementById('email');
let password=document.getElementById('password');
let repassword=document.getElementById('repassword');
let signUpBtn=document.getElementById('signUpBtn');


const signUpForm = document.getElementById('signUpForm');
signUpForm.addEventListener('submit', (event) => {
    event.preventDefault(); 

})



// //name Validation

// fullName.onsubmit= function nameValidation(){
//     let nameRegex=/^([A-ZÀ-ÿ][-,a-z. ']+[ ]*)$/;
//     let valResult=nameRegex.test(fullName.value);

//     if(valResult==false){
//         console.log("wrong input")
//         fullName.style.backgroundColor='#ff9999';

//     }
//     return true;      
// }


// //userName Validation

// userName.onkeyup= function userNameValidation(){
//     let nameRegex=/^[0-9A-Za-z]{6,16}$/;
//     let valResult=nameRegex.test(userName.value);
//     if(valResult==false){
//         console.log("wrong input")
//         userName.style.backgroundColor='#ff9999';

//     }else{
//     localStorage.setItem("userName",userName.value);
//     return true;
//     }
// }


// //Email Validation

// userEmail.onkeyup=function emailValidation(){
//     let emailRegex=/^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
//     let valresult=emailRegex.test(userEmail.value);

//     if(valresult==false){
//         console.log("wrong input")
//         userEmail.style.backgroundColor='#ff9999';

//     }
//     return true;
// }



//     //Password Validation

//     password.onkeyup=function passValidation(){
//         let passwordRegex=/^(?=.*\d)(?=.*[a-z])[0-9a-zA-Z]{8,}$/;
//         let valresult=passwordRegex.test(password.value);

//         if(valresult==false){
//             console.log("wrong input")
//             password.style.backgroundColor='#ff9999';
//         }
//         return true;
//     }


//     //repassword validation

//     repassword.onkeyup=function confirmPassword() {
//         if (password.value!== repassword.value) {
           
//            console.log('Passwords do not match.');
//            repassword.placeholder='Passwords do not match.';

//         } else {
//            console.log('great'); 
//         }
//     }


