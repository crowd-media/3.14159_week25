<div class="container">
  <div class="setup">
    <label class = "justify-flex">
      <span>Add your topic:</span>
      <input class="margin-20"/>
    </label>

    <div class="grid"> 
      <div class="box-style grid_column_left"> 
          <br/>
          <br/>
          form agent 1<br/>
          <br/>
          <br/>
      </div>
      
      <div class="box-style grid_column_right"> 
          <br/>
          <br/>
          form agent 2<br/>
          <br/>
          <br/>
      </div>
  </div> 
  
  <button class="box-style generate-promps">
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
  