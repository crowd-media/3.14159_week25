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
