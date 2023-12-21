<script>
	const energy_list = ['Assertive', 'Passive', 'Aggressive', 'Manipulative'];
	export let selected = energy_list[0];
	$: console.log(selected)
</script>


<div class="button-container">
	{#each energy_list as energy}
		<button
			aria-current={selected === energy}
			on:click={() => selected = energy}
		>{energy}</button>
	{/each}
</div>


<style>
	.button-container {
		
		display: grid;
		grid-template-columns: repeat(4, 1fr);
		grid-gap: 5px;
	  	
	}
	button[aria-current="true"] {
		transform: none;
		filter: none;
		box-shadow: inset 10px 10px 10px rgba(0, 0, 0, 0.2);
	}
  </style>