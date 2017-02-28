package com.example.selenatan.iotsmartscale;

public class userIntake{
    public int id;
    public String date, energy, fat, saturates, carbohydrate, sugars, fibre, protein, salt;

    public userIntake (int Id, String Date, String Energy, String Fat, String Saturates, String Carbohydrate, String Sugars, String Fibre, String Protein, String Salt){
        this.id = Id;
        this.date = Date;
        this.energy = Energy;
        this.fat = Fat;
        this.saturates = Saturates;
        this.carbohydrate = Carbohydrate;
        this.sugars = Sugars;
        this.fibre = Fibre;
        this.protein = Protein;
        this.salt = Salt;
    }

    public userIntake (){
        this(-1,"","","","","","","","","");
    }
}
