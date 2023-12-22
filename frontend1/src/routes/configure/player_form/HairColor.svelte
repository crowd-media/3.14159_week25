<script>
	const hair_color_types = [
		"black",
		"brown",
		"blond",
		"white/gray",
		"rarely red",
	];
	export let selected = hair_color_types[0];
</script>

<div class="button-container">
	{#each hair_color_types as hair_color}
		<button
			class:selected={selected === hair_color}
			on:click={() => (selected = hair_color)}>{hair_color}</button
		>
	{/each}
</div>

<style>
	.button-container {
		display: grid;
		grid-template-columns: repeat(5, 1fr);
		grid-gap: 5px;
	}

	button {
		border: none;
		padding: 5px;
		border-radius: 3px;
		cursor: pointer;
	}
	.selected {
		background-image: linear-gradient(
			109.6deg,
			hsl(94, 94%, 72%) 11.2%,
			rgba(24, 138, 141, 1) 91.1%
		);
		color: white;
	}
</style>
