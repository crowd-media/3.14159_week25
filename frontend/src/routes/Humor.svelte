<script>
	const humor_types = ['Ironical', 'Absurd', 'Neutral','Serious'];
	let selected = humor_types[0];
</script>


<div class="button-container">
	{#each humor_types as humor}
		<button
			on:click={() => selected = humor}
		>{humor}</button>
	{/each}
</div>

<style>
	.button-container {
	  display: flex;
	  justify-content: center;
	}
  </style>