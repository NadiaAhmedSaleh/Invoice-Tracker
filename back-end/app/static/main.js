

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
