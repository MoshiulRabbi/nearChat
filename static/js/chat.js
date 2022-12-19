//id of the other user, name for now
const other_user_name = JSON.parse(
  document.getElementById("other_user_name").textContent
);

// id of the user id, name for now
const user_id = JSON.parse(document.getElementById("user_id").textContent);

const chatSocket = new WebSocket(
  "ws://" + window.location.host + "/ws/" + other_user_name + "/"
);
chatSocket.onopen = function (e) {
  console.log("Connection Established");
};

chatSocket.onclose = function (e) {
  console.log("CONNECTION LOST");
};
chatSocket.onmessage = function (e) {
  const data = JSON.parse(e.data);

  if (data.username == user_id) {
    document.querySelector(".messanger-list").innerHTML += `<li class="repaly">
    <p> ${data.message} </p>
     <span class="time">10:32 am</span>
    </li>`;
  } else {
    document.querySelector(".messanger-list").innerHTML += `<li class="sender">
    <p> ${data.message} </p>
     <span class="time">10:32 am</span>
    </li>`;
  }

  // Get the .messanger-list element
  var messageList = document.querySelector(".messanger-list");

  // Scroll the element into view
  messageList.lastElementChild.scrollIntoView();
};

chatSocket.onclose = function (e) {
  console.error("Chat socket closed unexpectedly");
};

document.addEventListener("DOMContentLoaded", function () {
  // Get the #message-box element
  var messageBox = document.querySelector("#message-box");
  // Give it focus
  messageBox.focus();

  // Add an event listener for the onkeyup event
  messageBox.onkeyup = function (e) {
    // If the key pressed is the enter key
    if (e.keyCode === 13) {
      // Simulate a click on the #submit-button element
      document.querySelector("#submit-button").click();
    }
  };
});

document.querySelector("#submit-button").onclick = function (e) {
  const messageInputDom = document.querySelector("#message-box");
  const message = messageInputDom.value;
  chatSocket.send(
    JSON.stringify({
      message: message,
      username: user_id,
    })
  );
  messageInputDom.value = "";
};
