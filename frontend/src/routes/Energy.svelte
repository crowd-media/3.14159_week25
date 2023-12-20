<script>
	const colors = ['Assertive', 'Passive', 'Aggressive', 'Manipulative'];
	let selected = colors[0];
</script>


<div>
	{#each colors as color}
		<button
			on:click={() => selected = color}
		>{color}</button>
	{/each}
</div>