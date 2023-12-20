<script>
	import Age from './Age.svelte';
	import Energy from './Energy.svelte'
	import Role from './Role.svelte';
	import Humor from './Humor.svelte';
	import Aptitude from './Aptitude.svelte';
	import welcome from '$lib/images/svelte-welcome.webp';
	import welcome_fallback from '$lib/images/svelte-welcome.png';
</script>

<svelte:head>
	<title>Configuracion jugador</title>
	<meta name="description" content="Svelte demo app" />
</svelte:head>

<section>
	<h1>
		<p>Configure your player personality</p>
	</h1>
	<div>
		<h2>
			How old are your player?
		</h2>
		<Age />

	</div>
	<div>
		<h2>
			Choose the communication type of your player
		</h2>
		<div class=button-container>
			<Energy />
		</div>
		

	</div>
	<div>
		<h2>
			How do you define your player?
		</h2>
		<div class=button-container>
			<Role />	
		</div>
		

	</div>
	<div>
		<h2>
			Choose your player's sense of humor
		</h2>
		<div class=button-container>
			<Humor />
		</div>

	</div>
	<div>
		<h2>
			Choose the main skill or ability
		</h2>
		<div class=button-container>
			<Aptitude />
		</div>
		

	</div>
	
	
</section>

<style>
	.button-container {
	  display: flex;
	  justify-content: center;
	}
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
	h2 {
		color: rgb(47, 47, 47);
    	font-weight:lighter;
   	 	text-align: center;
		font-size: 30px;
    	font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
		width: 100%;
	}
	
</style>
