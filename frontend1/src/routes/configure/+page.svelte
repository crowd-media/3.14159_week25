<script>
  import PlayerDescription from "./player_form/PlayerDescription.svelte";

  let player1_info={
        age:1,
		    hair_color:"",
        energy:"",
        role: "",
        aptitude:"",
        humor:""
    };
  
  let player2_info={
        age:1,
		    hair_color:"",
        energy:"",
        role: "",
        aptitude:"",
        humor:""
    };

  let body_config={
		topic:"",
		word_limit:50,
		first_agent:{
			name: "",
			characteristics:[]
		},
		second_agent:{
			name: "",
			characteristics:[]
		}
  };

  var raw = JSON.stringify({
		"topic": "Who is the better one of us",
		"word_limit": 50,
		"first_agent": {
			"name": "Juju",
			"characteristics": [
			"age = 27",
			"humor=serious",
			"mood=sweet,emotional,loving,hungry,perfect,analytic,open-minded"
			]
		},
		"second_agent": {
			"name": "Momo",
			"characteristics": [
			"age = 30",
			"hair=brown",
			"eyecolor=brown",
			"mood=emotional, not balanced, hateful"
			]
		}
		});

  async function handleSubmit() {
		console.log(raw)
		// body_config.first_agent.name=player1_info.player_name
		// let characteristics= Object.keys(player1_info).map(key => `${key}=${player1_info[key]}`);
		// body_config.first_agent.characteristics = characteristics
		
		console.log(body_config)
		const response = await fetch("http://localhost:8000/configuration", {
					"headers": {
						"accept": "application/json",
						"accept-language": "en-US,en;q=0.9",
						"sec-ch-ua": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\", \"Microsoft Edge\";v=\"120\"",
						"sec-ch-ua-mobile": "?1",
						"sec-ch-ua-platform": "\"Android\"",
						"sec-fetch-dest": "empty",
						"sec-fetch-mode": "cors",
						"sec-fetch-site": "same-origin"
					},
					"referrer": "http://localhost:8000/docs",
					"referrerPolicy": "strict-origin-when-cross-origin",
					"body": raw,
					"method": "POST",
					"mode": "cors",
					"credentials": "omit"
					});
		console.log(response)
		const respiri = await response.json()
		
	}
</script>


<div class="container">
  <div class="setup">
    <label class = "justify-flex">
      <span>Add your topic:</span>
      <input class="margin-20" bind:value={body_config.topic}/>
    </label>

    <div class="grid"> 
      <div class="box-style grid_column_left"> 
        <PlayerDescription bind:player_info={player1_info}/>
      </div>
      
      <div class="box-style grid_column_right"> 
        <PlayerDescription bind:player_info={player2_info}/>
      </div>
  </div> 
  
  <button class="box-style generate-promps" on:click={handleSubmit}>
    <p>GENERATE AGENTS DESCRIPTIONS!</p>
  </button>

  <p> Prompt prefix</p>
  <textarea rows="8" class="box-style width-100">
  </textarea>
  
  <div class="grid"> 
    <p> Prompt agent 1</p>
    <textarea rows="10" class="box-style grid_column_left"> 
    </textarea>
    <p> Prompt agent 2</p>
    <textarea rows="10" class="box-style grid_column_right"> 
    </textarea>
  </div> 
  
  <p> Referee First Message</p>
  <textarea rows="8" class="box-style width-100">
  </textarea>
  
  <p> Conversation ID</p>
  <textarea class="box-style width-100">
  </textarea>
  
  <button class="box-style generate-promps">
    <p> Save Config</p>
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

	.setup {
	  display: flex;
	  flex-direction: column;
	  width: 100%;
    padding: 20px;
    box-sizing: border-box;
	  align-self: center;
	}

  button{
    border:none;
    font-size: 15px;
    width: 100%;
  }

  button:hover{
    cursor: pointer;
    opacity: 0.9;
  }

  .width-100{
    width: 100%;
  }

  .margin-20{
      size: 10px; 
      width: 240px;
  }
  .grid{
    display: grid;
    grid-template-columns: 1fr 1fr;
    grid-gap: 10px;
  }

  .justify-flex{
    display: flex;
    flex-direction: row;
    justify-content: center;
    gap: 20px;
  }

  .box-style{
    box-shadow: 6px 6px 10px rgba(34, 34, 34, 0.2), -6px -6px 10px #fff;
    border-radius: 20px;
    padding: 10px;
    box-sizing: border-box;
    display: flex;
    justify-content: center;
    align-items: center;
  }
  .grid_column_left{
    grid-row: 3;
    grid-column: 1;
  }
  .grid_column_right{
    grid-row: 3;
    grid-column: 2;
  }

  .generate-promps{
      background-color: rgb(255, 159, 103);
      margin: 30px auto;
  }
  </style>
  