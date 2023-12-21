<script>
	const humor_types = ['Ironical', 'Absurd', 'Neutral','Serious'];
	export let selected = humor_types[0];
</script>


<div class="button-container">
	{#each humor_types as humor}
		<button
			aria-current={selected === humor}
			on:click={() => selected = humor}
		>{humor}</button>
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