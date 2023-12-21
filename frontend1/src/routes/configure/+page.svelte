<p>Add your topic:</p>
<input class="topic"/>

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

<div class="box-style generate-promps">
    <button>
      <p>GENERATE AGENTS DESCRIPTIONS!:)</p>
    </button>
</div>

<p> Prompt prefix</p>
<textarea>
</textarea>

<div class="grid"> 
  <p> Prompt agent 1</p>
  <textarea class="box-style grid_column_left"> 
  </textarea>
  <p> Prompt agent 2</p>
  <textarea class="box-style grid_column_right"> 
  </textarea>
</div> 

<p> Referee First Message</p>
<textarea>
</textarea>

<p> Conversation ID</p>
<textarea>
</textarea>

<button class="box-style generate-promps">
  <p> Save Config</p>
</button>

       
    
<style>
  .topic{
      box-shadow: 6px 6px 10px rgba(34, 34, 34, 0.2), -6px -6px 10px #fff;
      padding: 10px;
      box-sizing: border-box;
      border-radius: 20px;
      margin: 20px auto; 
  }
  .grid{
    display: grid;
    grid-template-columns: 1fr 1fr;
    grid-gap: 20px;
  }

  /* display: flex;
    justify-content: center;
    align-items: center;
    TODO: Put out of this style so the box-style can be reused*/

  .box-style{
    box-shadow: 6px 6px 10px rgba(34, 34, 34, 0.2), -6px -6px 10px #fff;
    border-radius: 20px;
    padding: 10px;
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
  