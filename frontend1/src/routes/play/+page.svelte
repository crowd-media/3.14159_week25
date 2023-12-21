<script>
  let socket;
  let conversation_id = "ai_uprising";
  /**
   * @type {any[]}
   */
  let messagesFromServer = [];
  const addToArray = (/** @type {{ time: Date; data: any; }} */ message) => {
    messagesFromServer = [...messagesFromServer, message];
  };
  const handlePlay = async () => {
    // Here we recieve a callback whenever new data is pushed into the store
    socket = new WebSocket(`ws://127.0.0.1:8000/ws/${conversation_id}/5`);
    messagesFromServer = [];
    socket.addEventListener("open", () => {
      console.log("Opened");
    });
    socket.addEventListener("message", function (event) {
      console.log(event.data);
      addToArray({ time: new Date(), data: JSON.parse(event.data) }); // When the server respons with a message we save it in an array
    });
  };

  $: console.log({ messagesFromServer });
</script>

<div class="container">
  <div class="chat">
    <p>Select conversation id</p>
    <input bind:value={conversation_id} placeholder="Conversation ID" />
    <button on:click={handlePlay}>Play</button>
    {#each messagesFromServer as message}
      {#if message.data.message === "conversation_finish"}
        <span class="agent">Conversation finished</span>
      {:else}
        <div class={message.data.speaker} class:agent={true}>
          <!-- <p>
				  {new Date(message.time).toISOString()}
				</p> -->
          <p>
            {message.data.text}
          </p>
          {#if message.data.url}
            <audio controls>
              <source src={message.data.url} type="audio/mp3" />
              Your browser does not support the audio element.
            </audio>
          {/if}
        </div>
      {/if}
    {/each}
  </div>
</div>

<style>
  .container {
    display: flex;
    flex-direction: column;
    overflow-y: scroll;
    width: 100vw;
    align-self: center;
  }
  .chat {
    display: flex;
    flex-direction: column;
    max-width: 500px;
    align-self: center;
  }
  .agent {
    width: 80%;
    margin: 10px;
    padding: 10px;
    border-radius: 5px;
  }
  .agent_1 {
    background-color: aliceblue;
    align-self: flex-start;
  }

  .agent_2 {
    background-color: antiquewhite;
    align-self: flex-end;
  }

  .referee {
    background-color: aquamarine;
    align-self: center;
  }
</style>
