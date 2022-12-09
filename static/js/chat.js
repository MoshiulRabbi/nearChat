//id of the other user, name for now
const other_user_id = JSON.parse(
  document.getElementById("other_user_id").textContent
);

// id of the user id, name for now
const user_id = JSON.parse(document.getElementById("user_id").textContent);

const chatSocket = new WebSocket(
  "ws://" + window.location.host + "/ws/" + other_user_id + "/"
);
chatSocket.onopen = function (e) {
  console.log(user_id);
  console.log(other_user_id);
};

chatSocket.onclose = function (e) {
  console.log("CONNECTION LOST");
};
chatSocket.onmessage = function (e) {
  const data = JSON.parse(e.data);
  console.log(data);
  // document.querySelector("#chat-log").value += data.message + "\n";

  document.querySelector(
    ".messanger-list"
  ).innerHTML += `<li id="chat-log" class="common-message is-you">
        <p class="common-message-content">
          ${data.message}<br /><br />
        </p>
        <span class="status is-seen">✔️✔️</span>
        <time datetime>14:41</time>
      </li>`;
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
    })
  );
  messageInputDom.value = "";
};
