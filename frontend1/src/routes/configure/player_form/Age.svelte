<script>
	export let age = 15;
</script>

<label>
	<input type="number" bind:value={age} min="0" max="100" />
	<input type="range" bind:value={age} min="0" max="100" />
</label>

