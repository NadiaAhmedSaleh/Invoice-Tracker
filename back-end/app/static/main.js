//get email from local storage

function splitEmail(email) {
  let namePart = email.split('@')[0];
  let nameArray = namePart.split(/[._]/); 
  let formattedName = nameArray.map(word => word.charAt(0).toUpperCase() + word.slice(1)).join(' ');

  return formattedName;
}

let savedName = splitEmail(localStorage.getItem("email"));

document.getElementById('displayValue').innerText = "Welcome " + savedName ;

// Configuration object for the fetch request
const options = {
  method: "DELETE",
  credentials: "include",
};



// Send the DELETE request using fetch
function deleteInvoice(id) {
  fetch(`http://localhost:5000/invoices/delete/${id}`, options)
    .then((response) => {
      if (!response.ok) {
        throw new Error("Network response was not ok");
      } else {
        window.location.reload();
      }
    })
    .catch((error) => {
      console.error(
        "There was a problem with the DELETE request:",
        error.message
      );
    });
}

const markOptions = {
  method: "PUT",
  credentials: "include",
};

function markInvoiceAsPaid(id) {
  res = fetch(`http://localhost:5000/invoices/mark-as-paid/${id}`, markOptions)
    .then((response) => {
      if (!response.ok) {
        throw new Error("Network response was not ok");
      } else {
        window.location.reload();
      }
    })
    .catch((error) => {
      console.error(
        "There was a problem with the DELETE request:",
        error.message
      );
    });
}



