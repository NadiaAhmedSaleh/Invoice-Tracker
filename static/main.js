
//welcome header

const userName = localStorage.getItem("userName");
document.getElementById("welcome").innerHTML="Welcome " + userName;


//calling apis from backend

let invoices=[];
let totalNumber=document.getElementById("totalNumber")


//get all invoices 

async function getInvoices(){
    const response=await fetch('http://localhost:5000/invoices/list');
    const finalResponse=await response.json();
    invoices=finalResponse.invoices;
    displayInvoices(invoices);

}

/////////////////////////////////////////////////////////////

//display invoices

let invoicesRow=document.getElementById('invoicesRow');

function displayInvoices(invoices){
    let container="";
    for(let i=0 ; i<=invoices.length-1; i++){
        container+=`

        <tr>
        <td>#${invoices[i]?.id}</td>
        <td>${invoices[i]?.issuer}</td>
        <td><B>${invoices[i]?.amount}</B></td>
        <td>${invoices[i]?.due_date}</td>
        <td><a class="statues">${invoices[i]?.status}</a></td>
        <td> <button class="deleteBtn" id="deleteBtn" onclick="deleteInvoice(2)">Delete</button> </td>
        
        
        `
    }


    totalNumber.innerHTML="There are " + invoices.length + " in total"

    invoicesRow.innerHTML=container
}

getInvoices();

/////////////////////////////////////////////////////////////

//get text inside the select options 
/*
let statusInput=document.getElementById('statusInput').value;
let option="";


//display filtered invoices


let filteredInvoices=[];

async function getFilteredInvoices(statusInput){
    const response=await fetch(`http://127.0.0.1:5000/invoices/list/?status=${statusInput}`);
    const finalResponse=await response.json();
    filteredInvoices=finalResponse;
    console.log(filteredInvoices);

    displayInvoices(filteredInvoices)

}

*/
/////////////////////////////////////////////////////////////

//create invoice

//click on button add
//redirect to the add page
let addBtn=document.getElementById('addBtn');
function toCreateInvoice(){
    window.location.href="file:///D:/Invoice%20Tracker/Invoice-Tracker/front-end/addInvoice.html";
    
}

// call add api once the submit button is clicked




///////////////////////////////////////////////////////////

//mark as paid

//click on status button
//if status == pending
//call the mark as paid api
//change the style of the button






//delete invoice

//on click on button and call the api


let deleteBtn=document.getElementById("deleteBtn")


async function deleteInvoice(id){
    const response=await fetch(`http://127.0.0.1:5000/invoices/delete/${id}`);
    console.log('Delete successful')
    

}




///////////////////////////////////////////
//change the style of the button

function changeStatus(){

    let sliderBtn=document.getElementById("sliderBtn");
    if(sliderBtn.innerText=='Pending'){

        sliderBtn.innerText='Paid'
    }else{

        sliderBtn.innerText='Pending'
    }
    
    
}



///////////////////////////////////////////////////////

