<svelte:head>
	<title>Game Configuration</title>
	<meta name="description" content="Configure the player personality and the game" />
</svelte:head>

<script>
	
	import PlayerDescription from "./PlayerDescription.svelte";
	
	let player1_info={
		player_id:"1",
        age:1,
		hair_color:"",
        energy:"",
        role: "",
        aptitude:"",
        humor:""
    };
	let player2_info={
		player_id:"2",
        age:1,
		hair_color:"",
        energy:"",
        role: "",
        aptitude:"",
        humor:""
    }
	function handleSubmit() {

		JSON.stringify([player1_info,player2_info])
		console.log(JSON.stringify([player1_info,player2_info]))
	}

</script>


<section>
	<h1>
		<p>Configure your player personality</p>
	</h1>
	<form on:submit={handleSubmit}>

	
	<h1>
		Player {player1_info.player_id}
	</h1>
	<PlayerDescription bind:player_info={player1_info}/>
	<div class='button-submit'>
		<input type="submit" name="submit" value="submit button" />
	</div>
	</form>
	

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
