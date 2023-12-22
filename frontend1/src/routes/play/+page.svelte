<script>
	let socket;
	let conversation_id = '';
	/**
	 * @type {any[]}
	 */
	let messagesFromServer = [];
	const addToArray = (/** @type {{ time: Date; data: any; }} */ message) => {
		messagesFromServer = [...messagesFromServer, message];
	};

	let ws_connected = false;
	const handlePlay = async () => {
		// Here we recieve a callback whenever new data is pushed into the store
		socket = new WebSocket(`ws://34.250.204.68:8000/ws/${conversation_id}/5`);
		ws_connected = true;
		messagesFromServer = [];
		socket.addEventListener('open', () => {
			console.log('Opened');
		});
		socket.addEventListener('message', function (event) {
			console.log(event.data);
			addToArray({ time: new Date(), data: JSON.parse(event.data) }); // When the server respons with a message we save it in an array
		});
		socket.addEventListener('close', () => (ws_connected = false));
	};

	$: console.log({ messagesFromServer });
</script>

<div class="container">
	<div class="chat">
		<label class="justify-flex-column">
			<span>Write your conversation ID</span>
			<input class="conversation-id" bind:value={conversation_id} placeholder="Conversation ID" />
			<button class="conversation-id" on:click={handlePlay} disabled={ws_connected}>Play</button>
		</label>

		{#each messagesFromServer as message}
			{#if message.data.message === 'conversation_finish'}
				<div class="conv-finished"><span class="agent">Conversation finished</span></div>
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
	.conv-finished {
		margin: 20px;
		align-self: center;
		text-align: center;
	}

	.justify-flex-column {
		display: flex;
		flex-direction: column;
		justify-content: center;
		gap: 10px;
		padding: 15px;
		box-sizing: border-box;
	}
	.conversation-id {
		align-self: center;
		width: 250px;
		text-align: center;
	}

	input {
		font-size: 15px;
	}

	button {
		font-size: 17px;
	}

	button:disabled {
		opacity: 0.5;
	}

	button:hover {
		cursor: pointer;
		color: rgba(24, 138, 141, 1);
	}

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
		width: 100%;
		padding: 20px;
		box-sizing: border-box;
		align-self: center;
		--radius-big: 20px;
		--radius-small: 6px;
	}
	.agent {
		width: 80%;
		margin: 10px;
		padding: 10px;
		border-radius: 5px;
		box-shadow:
			6px 6px 10px rgba(34, 34, 34, 0.2),
			-6px -6px 10px #fff;
	}

	.agent_1 {
		text-align: left;
		background-color: rgba(24, 138, 141, 1);
		color: white;
		align-self: flex-start;
		border-radius: var(--radius-big) var(--radius-big) var(--radius-big) var(--radius-small);
	}

	.agent_2 {
		text-align: right;
		background-color: hsl(0, 0%, 43%);
		align-self: flex-end;
		color: white;
		border-radius: var(--radius-big) var(--radius-big) var(--radius-small) var(--radius-big);
	}

	.referee {
		background-color: rgb(255, 136, 0);
		align-self: center;
		color: white;
		border-radius: var(--radius-big);
	}
</style>
