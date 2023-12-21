<script>
	const hair_color_types = ['black', 'brown', 'blond','white/gray','rarely red'];
	export let selected = hair_color_types[0];
</script>


<div class="button-container">
	{#each hair_color_types as hair_color}
		<button
			aria-current={selected === hair_color}
			on:click={() => selected = hair_color}
		>{hair_color}</button>
	{/each}
</div>

<style>
	.button-container {
		
		display: grid;
		grid-template-columns: repeat(5, 1fr);
		grid-gap: 5px;
	  	
	}
	button[aria-current="true"] {
		transform: none;
		filter: none;
		box-shadow: inset 10px 10px 10px rgba(0, 0, 0, 0.2);
	}
  </style>