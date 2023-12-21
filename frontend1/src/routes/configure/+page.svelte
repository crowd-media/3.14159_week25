<script>
	import PlayerDescription from "./player_form/PlayerDescription.svelte";

	let player1_info = {
		age: 1,
		name: "",
		hair_color: "",
		energy: "",
		role: "",
		aptitude: "",
		humor: "",
	};

	let player2_info = {
		age: 1,
		name: "",
		hair_color: "",
		energy: "",
		role: "",
		aptitude: "",
		humor: "",
	};

	let body_config = {
		topic: "",
		word_limit: 50,
		first_agent: {
			name: "",
			characteristics: [],
		},
		second_agent: {
			name: "",
			characteristics: [],
		},
	};

	let description_response = {
		first_statement: "",
		prompt_prefix: "",
		agent_1: "",
		agent_2: "",
	};

	let configuration_id = "";

	async function handleDescriptionSubmit() {
		const raw = JSON.stringify({
			topic: body_config.topic,
			word_limit: body_config.word_limit,
			first_agent: {
				name: player1_info.name,
				characteristics: Object.keys(player1_info).map(
					// @ts-ignore
					(key) => `${key}=${player1_info[key]}`,
				),
				model: "gpt-4",
			},
			second_agent: {
				name: player2_info.name,
				characteristics: Object.keys(player2_info).map(
					// @ts-ignore
					(key) => `${key}=${player2_info[key]}`,
				),
				model: "gpt-4",
			},
		});

		console.log("LETS FETCH");
		console.log(raw);

		console.log(body_config);
		try {
			const response = await fetch("http://127.0.0.1:8000/descriptions", {
				headers: {
					"Content-Type": "application/json",
				},
				body: raw,
				method: "POST",
			});
			console.log(response);
			description_response = await response.json();
		} catch (e) {
			console.log(e);
			alert("error");
		}
	}

	async function handleConfigurationSubmit() {
		const raw = JSON.stringify({
			id: configuration_id,
			topic: body_config.topic,
			first_agent: {
				name: player1_info.name,
				characteristics: Object.keys(player1_info).map(
					// @ts-ignore
					(key) => `${key}=${player1_info[key]}`,
				),
				description: description_response.agent_1,
				model: "gpt-4",
			},
			second_agent: {
				name: player2_info.name,
				characteristics: Object.keys(player2_info).map(
					// @ts-ignore
					(key) => `${key}=${player2_info[key]}`,
				),
				description: description_response.agent_2,
				model: "gpt-4",
			},
			prompt_prefix: description_response.prompt_prefix,
			first_statement: description_response.first_statement,
		});

		console.log("LETS FETCH");
		console.log(raw);
		// body_config.first_agent.name=player1_info.player_name
		// let characteristics= Object.keys(player1_info).map(key => `${key}=${player1_info[key]}`);
		// body_config.first_agent.characteristics = characteristics

		console.log(body_config);
		const response = await fetch("http://127.0.0.1:8000/configuration", {
			headers: {
				"Content-Type": "application/json",
			},
			body: raw,
			method: "POST",
		});
		console.log(response);
		const respiri = await response.json();
	}
</script>

<div class="container">
	<div class="setup">
		<label class="justify-flex-row">
			<span>Add your topic:</span>
			<input class="margin-20" bind:value={body_config.topic} />
		</label>

		<div class="grid">
			<div class="box-style grid_column_left">
				<PlayerDescription bind:player_info={player1_info} />
			</div>

			<div class="box-style grid_column_right">
				<PlayerDescription bind:player_info={player2_info} />
			</div>
		</div>

		<button
			class="box-style generate-promps"
			on:click={handleDescriptionSubmit}
		>
			<p>GENERATE AGENTS DESCRIPTIONS!</p>
		</button>

		<p>Prompt prefix</p>
		<textarea
			rows="8"
			class="box-style width-100"
			bind:value={description_response.prompt_prefix}
		/>

		<div class="grid">
			<p>Prompt agent 1</p>
			<textarea
				rows="10"
				class="box-style grid_column_left"
				bind:value={description_response.agent_1}
			/>
			<p>Prompt agent 2</p>
			<textarea
				rows="10"
				class="box-style grid_column_right"
				bind:value={description_response.agent_2}
			/>
		</div>

		<p>Referee First Message</p>
		<textarea
			rows="8"
			class="box-style width-100"
			bind:value={description_response.first_statement}
		/>

		<label class="justify-flex-column">
			<span>Configuration ID</span>
			<textarea
				class="conversation-id box-style"
				bind:value={configuration_id}
			/>
		</label>

		<button
			class="box-style generate-promps"
			on:click={handleConfigurationSubmit}
		>
			<p>Save Config</p>
		</button>
	</div>
</div>

<style>
	.container {
		display: flex;
		flex-direction: column;
		overflow-y: scroll;
		width: 100vw;
		align-self: center;
	}

	.conversation-id {
		align-self: center;
		width: 500px;
		text-align: center;
	}

	.setup {
		display: flex;
		flex-direction: column;
		width: 100%;
		padding: 20px;
		box-sizing: border-box;
		align-self: center;
	}

	button {
		border: none;
		font-size: 15px;
		width: 100%;
	}

	button:hover {
		cursor: pointer;
		opacity: 0.9;
	}

	.width-100 {
		width: 100%;
	}

	.margin-20 {
		size: 10px;
		width: 240px;
	}
	.grid {
		display: grid;
		grid-template-columns: 1fr 1fr;
		grid-gap: 10px;
	}

	.justify-flex-row {
		display: flex;
		flex-direction: row;
		justify-content: center;
		gap: 20px;
	}

	.justify-flex-column {
		display: flex;
		flex-direction: column;
		justify-content: center;
		gap: 20px;
		margin: 20px;
	}

	.box-style {
		box-shadow:
			6px 6px 10px rgba(34, 34, 34, 0.2),
			-6px -6px 10px #fff;
		border-radius: 20px;
		padding: 10px;
		box-sizing: border-box;
		display: flex;
		justify-content: center;
		align-items: center;
	}
	.grid_column_left {
		grid-row: 3;
		grid-column: 1;
	}
	.grid_column_right {
		grid-row: 3;
		grid-column: 2;
	}

	.generate-promps {
		background-color: rgb(255, 159, 103);
		margin: 30px auto;
	}
</style>
