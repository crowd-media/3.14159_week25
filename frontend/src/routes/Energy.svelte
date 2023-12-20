<script>
	const colors = ['Assertive', 'Passive', 'Aggressive', 'Manipulative'];
	export let selected = colors[0];
	$: console.log(selected)
</script>


<div>
	{#each colors as color}
		<button
			on:click={() => selected = color}
		>{color}</button>
	{/each}
</div>