<script>
	const aptitude_types = ['Sceptical', 'Open-minded', 'Intolerant','Tolerant'];
	export let selected = aptitude_types[0];
</script>


<div>
	{#each aptitude_types as aptitude}
		<button
			on:click={() => selected = aptitude}
		>{aptitude}</button>
	{/each}
</div>
