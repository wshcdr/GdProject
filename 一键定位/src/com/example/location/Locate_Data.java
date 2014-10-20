package com.example.location;

import java.util.Timer;
import java.util.TimerTask;

import android.app.Service;
import android.content.ContentResolver;
import android.content.Intent;
import android.content.res.Configuration;
import android.os.IBinder;
import android.telephony.TelephonyManager;
import android.util.Log;

public class Locate_Data  extends Service{
	private String SIM_INFO;
	private int SIM_ID;
	@Override
	public IBinder onBind(Intent intent) {
		// TODO Auto-generated method stub
		Log.i("======", "开启服务");
		return null;
	}

	@Override
	public void onCreate() {
		// TODO Auto-generated method stub
		super.onCreate();
		//getSIM();
		Log.i("-------", "服务开启~");
		
	}

	@Override
	public void onStart(Intent intent, int startId) {
		// TODO Auto-generated method stub
		super.onStart(intent, startId);
	}

	@Override
	public int onStartCommand(Intent intent, int flags, int startId) {
		// TODO Auto-generated method stub
		Log.i("~~~", "service started");
		getSIM();
	
		return super.onStartCommand(intent, flags, startId);
		
	}

	@Override
	public void onConfigurationChanged(Configuration newConfig) {
		// TODO Auto-generated method stub
		super.onConfigurationChanged(newConfig);
	}
	public void getSIM(){
	TelephonyManager telMge=(TelephonyManager)getSystemService(TELEPHONY_SERVICE);
	int simState=telMge.getSimState();//状态
	String simSerialNumber=telMge.getSimSerialNumber();//卡号
	String simOperator=telMge.getSimOperator();//供货商号
	String simOperatorName=telMge.getSimOperatorName();//供货商名称
	String simCountryIso=	telMge.getSimCountryIso();//sim国别
	int phonType=	telMge.getPhoneType();//手机类型
	int netWorkType=	telMge.getNetworkType();//网络类型
	String netWorkOperatorName=	telMge.getNetworkOperatorName();//网络供应商名称
	String line1Number=	telMge.getLine1Number();//手机号码
	boolean networkRoaming=	telMge.isNetworkRoaming();//漫游
	int dataState=	telMge.getDataState();//数据类型
	String deviceSoftwareVersion=	telMge.getDeviceSoftwareVersion();//硬件软件版本
	String subScriberId=telMge.getSubscriberId();// 返回用户识别码（的IMSI）的设备
	
	ContentResolver cv = this.getContentResolver();
		String tmpS = "";//蓝牙是否开启
		tmpS = android.provider.Settings.System.getString(cv,android.provider.Settings.System.BLUETOOTH_ON);//WIFI是否开启
		tmpS = android.provider.Settings.System.getString(cv,android.provider.Settings.System.WIFI_ON);
		//飞行模式是否开启
		tmpS = android.provider.Settings.System.getString(cv,android.provider.Settings.System.AIRPLANE_MODE_ON);
		//数据漫游是否开启
		tmpS = android.provider.Settings.System.getString(cv,android.provider.Settings.System.DATA_ROAMING);
		SIM_INFO="{"+"\"SIM_ID\""+":"+(SIM_ID++)+","+"\"SIM_STATE\""+":"+simState+","+"\"SIM_SERIALNUMBER\""+":"+simSerialNumber
		+","+"\"SIM_OPERATER\""+":"+simOperator+","+"\"SIM_OPERATORNAME\""+":"+simOperatorName+","+"\"SIM_COUNTRYISO\""+":"+simCountryIso
		+"," +"\"PHONE_TYPE\""+":"+phonType+","+"\"NETWORK_TYPE\""+":"+netWorkType+","+"\"NETWORK_OPERATORNAME\""+":"+netWorkOperatorName+
			", "+"\"LINE1NUMBER\""+":"+line1Number+","+"\"NETWORKROAMING\""+":"+networkRoaming+","+"\"DATA_STATE\""+":"+dataState
			+"," +"\"DEVICESOFTWAREVERSION\""+":"+deviceSoftwareVersion+","+"\"SUB_SCRIBERID\""+":"+subScriberId+"}";
	Log.i("=======>", SIM_INFO);
	}
}
