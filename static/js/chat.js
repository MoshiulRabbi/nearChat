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
  console.log(user_id);
  console.log(other_user_name);
};

chatSocket.onclose = function (e) {
  console.log("CONNECTION LOST");
};
chatSocket.onmessage = function (e) {
  const data = JSON.parse(e.data);
  console.log(data);

  if (data.username == user_id) {
    // document.querySelector("#chat-log").value += data.message + "\n";

    document.querySelector(
      ".messanger-list"
    ).innerHTML += `<li class="repaly">
    <p> ${data.message} </p>
     <span class="time">10:32 am</span>
    </li>`;
  } else {
    document.querySelector(
      ".messanger-list"
    ).innerHTML += `<li class="sender">
    <p> ${data.message} </p>
     <span class="time">10:32 am</span>
    </li>`;
  }
};

chatSocket.onclose = function (e) {
  console.error("Chat socket closed unexpectedly");
};

document.querySelector("#message-box").focus();
document.querySelector("#message-box").onkeyup = function (e) {
  if (e.keyCode === 13) {
    // enter, return
    document.querySelector("#submit-button").click();
  }
};

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
