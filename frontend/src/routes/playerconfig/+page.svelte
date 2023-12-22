<svelte:head>
	<title>Game Configuration</title>
	<meta name="description" content="Configure the player personality and the game" />
</svelte:head>

<script>
	
	import PlayerDescription from "./PlayerDescription.svelte";
	
	let player1_info={
        age:1,
		hair_color:"",
        energy:"",
        role: "",
        aptitude:"",
        humor:""
    };
	let body_config={
		topic:"",
		word_limit:50,
		first_agent:{
			name: "",
			characteristics:[]
		},
		second_agent:{
			name: "",
			characteristics:[]
		}


	}
	var raw = JSON.stringify({
		"topic": "Who is the better one of us",
		"word_limit": 50,
		"first_agent": {
			"name": "Juju",
			"characteristics": [
			"age = 27",
			"humor=serious",
			"mood=sweet,emotional,loving,hungry,perfect,analytic,open-minded"
			]
		},
		"second_agent": {
			"name": "Momo",
			"characteristics": [
			"age = 30",
			"hair=brown",
			"eyecolor=brown",
			"mood=emotional, not balanced, hateful"
			]
		}
		});

	async function handleSubmit() {
		console.log(raw)
		body_config.first_agent.name=player1_info.player_name
		let characteristics= Object.keys(player1_info).map(key => `${key}=${player1_info[key]}`);
		body_config.first_agent.characteristics = characteristics
		
		console.log(body_config)
		const response = await fetch("http://34.250.204.68:8000/configuration/holi", {
					"headers": {
						"accept": "application/json",
						"accept-language": "en-US,en;q=0.9",
						"sec-ch-ua": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\", \"Microsoft Edge\";v=\"120\"",
						"sec-ch-ua-mobile": "?1",
						"sec-ch-ua-platform": "\"Android\"",
						"sec-fetch-dest": "empty",
						"sec-fetch-mode": "cors",
						"sec-fetch-site": "same-origin"
					},
					"referrer": "http://34.250.204.68:8000/docs",
					"referrerPolicy": "strict-origin-when-cross-origin",
					"body": null,
					"method": "GET",
					"mode": "cors",
					"credentials": "omit"
					});
		console.log(response)
		const respiri = await response.json()
		
	}

</script>


<section>
	
	<div class=topic>
		<p>Write the topic: </p>
		<input bind:value={body_config.topic} />
	</div>
	<h1>
		<p>Configure your player personality</p>
	</h1>
	<PlayerDescription bind:player_info={player1_info}/>

	<div class='button-submit'>
		<button on:click={handleSubmit}>
			Submit 
		</button>
	</div>
	

</section>

<style>
	section {
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		flex: 0.6;
	}

	h1 {
		color: grey;
    	font-weight:lighter;
   	 	text-align: center;
    	font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
		width: 75%;
	}
	.button-submit {
		padding: 10%;
		display: flex;
		justify-content: center;
	}
	
</style>
