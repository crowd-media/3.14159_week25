<script>
	const roles = ['Leader', 'Follower'];
	export let selected = roles[0];
</script>


<div class="button-container">
	{#each roles as role}
		<button
			aria-current={selected === role}
			on:click={() => selected = role}
		>{role}</button>
	{/each}
</div>

<style>
	.button-container {
		
		display: grid;
		grid-template-columns: repeat(2, 1fr);
		grid-gap: 5px;
	  	
	}
	button[aria-current="true"] {
		transform: none;
		filter: none;
		box-shadow: inset 10px 10px 10px rgba(0, 0, 0, 0.2);
	}
  </style>