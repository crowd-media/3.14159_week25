<script>
	const aptitude_types = ['Sceptical', 'Open-minded', 'Intolerant','Tolerant'];
	export let selected = aptitude_types[0];
</script>


<div class="button-container">
	{#each aptitude_types as aptitude}
		<button
			aria-current={selected === aptitude}
			on:click={() => selected = aptitude}
		>{aptitude}</button>
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
