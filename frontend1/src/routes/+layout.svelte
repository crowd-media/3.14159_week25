<script>
	import { goto } from "$app/navigation";
	import { page } from "$app/stores";
</script>

<main>
	<div class="header">
		<div class="botton_prompt">
			<button
				class:selected={$page.route.id == "/configure"}
				on:click={() => goto("configure")}
			>
				Configure
			</button>
		</div>
		<vline />
		<div class="botton_conversation">
			<button
				class:selected={$page.route.id == "/play"}
				on:click={() => goto("play")}
			>
				Converse
			</button>
		</div>
	</div>
	<h1>El Debate</h1>
	<slot />
</main>

<style>
	h1 {
		color: rgba(24, 138, 141, 1);
	}
	main {
		font-family: sans-serif;
		text-align: center;
		margin: 0px;
		overflow: hidden;
	}
	.header {
		text-align: center;
		box-shadow:
			6px 6px 10px rgba(34, 34, 34, 0.2),
			-6px -6px 10px #fff;
		padding: 10px;
		box-sizing: border-box;
		border-radius: 0px 0px 20px 20px;
		display: flex;
		flex-direction: row;
		justify-content: space-evenly;
		max-width: 300px;
		/* // align center */
		margin: 0px auto;
	}
	button {
		font-size: 20px;
		background-color: transparent;
		border: none;
		cursor: pointer;
	}

	.selected {
		color: rgba(24, 138, 141, 1);
	}
</style>
