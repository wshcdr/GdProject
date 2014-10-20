package com.example.location;

import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.preference.PreferenceActivity;
import android.widget.Toast;

public class ApprefenceActivity extends PreferenceActivity {
	protected void onCreate(Bundle paramBundle) {
		super.onCreate(paramBundle);
		addPreferencesFromResource(R.xml.mypreference);
		SharedPreferences localSharedPreferences = getSharedPreferences(
				"com.example.location_preferences", 0);
		String str1 = localSharedPreferences.getString("editNumPref", "110");
		Boolean localBoolean = Boolean.valueOf(localSharedPreferences
				.getBoolean("checkBoxPref_statelite", true));
		String str2 = localSharedPreferences.getString("editCityPref", "广州");
		String str3 = localSharedPreferences.getString("editDesPref", "广州塔");
		Intent localIntent = new Intent(this, MainActivity.class);
		localIntent.putExtra("NumToSend", str1);
		localIntent.putExtra("StateLite", localBoolean);
		localIntent.putExtra("DefProvince", str2);
		localIntent.putExtra("DefDestination", str3);
		
	}
}