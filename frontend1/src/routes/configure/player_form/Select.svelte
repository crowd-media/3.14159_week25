<script>
	export let options = [""];
	export let selected = options[0];
</script>

<div class="button-container">
	{#each options as option}
		<button
			class:selected={selected === option}
			on:click={() => (selected = option)}>{option}</button
		>
	{/each}
</div>

<style>
	.button-container {
		display: flex;
		justify-content: space-between;
		/* grid-gap: 5px; */
		width: 100%;
		flex-grow: 1;
	}

	button {
		display: flex;
		flex-grow: 1;
		margin: 0 5px;
		border: none;
		padding: 5px;
		border-radius: 3px;
		cursor: pointer;
		justify-content: center;
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
