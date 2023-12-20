<script>
	const roles = ['Leader', 'Follower'];
	export let selected = roles[0];
</script>


<div>
	{#each roles as role}
		<button
			on:click={() => selected = role}
		>{role}</button>
	{/each}
</div>