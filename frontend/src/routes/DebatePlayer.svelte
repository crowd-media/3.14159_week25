<script>
	import { spring } from 'svelte/motion';
	import { onMount } from 'svelte';

	let conv_id = ""

	let socket
	let messagesFromServer = []

	const addToArray = (message) => {
		console.log(event) 
		messagesFromServer = [...messagesFromServer, message] 	
	};

	const playConv = async () => {
		// Here we recieve a callback whenever new data is pushed into the store

		socket = new WebSocket(`ws://127.0.0.1:8000/ws/${conv_id}/5`)
  		socket.addEventListener("open", ()=> {
    	console.log("Opened")
	  	})

	  socket.addEventListener('message', function (event) {
  			addToArray({ time: new Date(), data: event.data }); // When the server respons with a message we save it in an array
		});

	}



</script>



<div >

	<p>Select conversation id</p>
	<input bind:value={conv_id}>
	<button on:click={playConv}>Play</button>

	{#each messagesFromServer as message}
	<div
	   id="slider"
	   class="slide-in orange"
	   v-for="message in messagesFromServer"
	   :key="message.time"
	 >
	   <ul>
		 <p>
		   { new Date(message.time).toISOString() }
		 </p>
		 <li>
		   { JSON.parse(message.data).text }
		   <audio controls>
			<source src={ JSON.parse(message.data).url } type="audio/mp3">
			Your browser does not support the audio element.
			</audio>
		
		 </li>
	   </ul>
	 </div>
	  {/each}


</div>

<style>
	.counter {
		display: flex;
		border-top: 1px solid rgba(0, 0, 0, 0.1);
		border-bottom: 1px solid rgba(0, 0, 0, 0.1);
		margin: 1rem 0;
	}

	.counter button {
		width: 2em;
		padding: 0;
		display: flex;
		align-items: center;
		justify-content: center;
		border: 0;
		background-color: transparent;
		touch-action: manipulation;
		font-size: 2rem;
	}

	.counter button:hover {
		background-color: var(--color-bg-1);
	}

	svg {
		width: 25%;
		height: 25%;
	}

	path {
		vector-effect: non-scaling-stroke;
		stroke-width: 2px;
		stroke: #444;
	}

	.counter-viewport {
		width: 8em;
		height: 4em;
		overflow: hidden;
		text-align: center;
		position: relative;
	}

	.counter-viewport strong {
		position: absolute;
		display: flex;
		width: 100%;
		height: 100%;
		font-weight: 400;
		color: var(--color-theme-1);
		font-size: 4rem;
		align-items: center;
		justify-content: center;
	}

	.counter-digits {
		position: absolute;
		width: 100%;
		height: 100%;
	}

	.hidden {
		top: -100%;
		user-select: none;
	}
</style>
