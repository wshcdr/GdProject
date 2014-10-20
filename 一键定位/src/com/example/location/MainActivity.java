package com.example.location;

import com.baidu.location.BDLocation;
import com.baidu.location.BDLocationListener;
import com.baidu.location.LocationClient;
import com.baidu.location.LocationClientOption;
import com.baidu.location.LocationClientOption.LocationMode;
import com.baidu.mapapi.SDKInitializer;
import com.baidu.mapapi.map.BaiduMap;
import com.baidu.mapapi.map.BitmapDescriptor;
import com.baidu.mapapi.map.BitmapDescriptorFactory;
import com.baidu.mapapi.map.MapStatusUpdate;
import com.baidu.mapapi.map.MapStatusUpdateFactory;
import com.baidu.mapapi.map.MapView;
import com.baidu.mapapi.map.MyLocationConfiguration;
import com.baidu.mapapi.map.MyLocationData;
import com.baidu.mapapi.model.LatLng;
import com.baidu.mapapi.navi.BaiduMapNavigation;
import com.baidu.mapapi.search.core.SearchResult;
import com.baidu.mapapi.search.geocode.GeoCodeOption;
import com.baidu.mapapi.search.geocode.GeoCodeResult;
import com.baidu.mapapi.search.geocode.GeoCoder;
import com.baidu.mapapi.search.geocode.OnGetGeoCoderResultListener;
import com.baidu.mapapi.search.geocode.ReverseGeoCodeResult;
import com.baidu.navisdk.BNaviEngineManager.NaviEngineInitListener;
import com.baidu.navisdk.BaiduNaviManager;
import com.baidu.navisdk.BaiduNaviManager.OnStartNavigationListener;
import com.baidu.navisdk.comapi.routeplan.RoutePlanParams.NE_RoutePlan_Mode;

import android.support.v7.app.ActionBarActivity;
import android.support.v7.app.ActionBar;
import android.support.v4.app.Fragment;
import android.telephony.TelephonyManager;
import android.telephony.gsm.SmsManager;
import android.telephony.gsm.SmsMessage;
import android.app.Activity;
import android.app.PendingIntent;
import android.content.ContentResolver;
import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.location.Geocoder;
import android.media.ExifInterface;
import android.net.Uri;
import android.os.Bundle;
import android.os.Environment;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Toast;
import android.os.Build;

public class MainActivity extends ActionBarActivity implements OnGetGeoCoderResultListener {
	/*��ǰ�����������£�
	 * 1�����ߵ�ͼ������·���滮 
	 * 2����service�н��ж�λ�����һ��ʱ���Զ���λ��
	 * 3�������������Զ�������λ���񣬣����Թ��������ݼ�¼ ����¼����json��ʽ����ϴ���
	 * 4������ĳЩ���ܿ����ڿ����������Զ����У������ݼ�¼���ϴ���
	 * 5��ʵʱ��Ч���ܣ�����������������ø��ĺ��ڳ������ܹ����ϵõ�Ӧ�ø��ĺ���Ӧ�ķ�Ӧ
	 * 6��ʹ��Alarm���г��򼤻��broadcast reciverһ��ʹ��
	 * Ŀǰ��Ҫ���й��ܰ��룬��ͬ���ܷ��ڲ�ͬ����
	 * */
	MapView mMapView;
	BaiduMap mBaiduMap;
	public LocationClient mLocationClient = null;
	public MyLocationListener myListener = new MyLocationListener();
	public StringBuffer sb;
	public Boolean isFirstPoi = true;
	BitmapDescriptor mCurrentMarker;
	public MyLocationConfiguration.LocationMode currentMode;
	public Boolean mIsEngineInitSuccess=false;
	private SharedPreferences preferences;
	public Boolean isStateLiteOn;//�Ƿ������ǵ�ͼ
	private String defCity,defDestination;//Ĭ�ϳ��к���ϸ��ַ
	private String mapZoomBy;//���õ�ͼ���ż���
	private double LOCATE_LATITITUDE,LOCATE_LONGTITUDE;//��ǰ��λλ�õľ�γ��
	private String LOCATITON_NOW;//��ǰλ��
	private String LOCATION_INFOMATION;
	private double DESTINATION_LATITUDE,DESTINATION_LONGTITUDE;
	private NaviEngineInitListener mNaviEngineInitListerner=new NaviEngineInitListener() {
		
		@Override
		public void engineInitSuccess() {
			// TODO Auto-generated method stub
			mIsEngineInitSuccess=true;
		}
		
		@Override
		public void engineInitStart() {
			// TODO Auto-generated method stub
			
		}
		
		@Override
		public void engineInitFail() {
			// TODO Auto-generated method stub
			
		}
	};
	private String getSdcardDir(){
		if(Environment.getExternalStorageState().equalsIgnoreCase(Environment.MEDIA_MOUNTED)){
			return Environment.getExternalStorageDirectory().toString();
		}
		return null;
	}
	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
	SDKInitializer.initialize(getApplicationContext());
		BaiduNaviManager.getInstance().initEngine(
				this, getSdcardDir(),mNaviEngineInitListerner, "r8XZhyHuSN7bsfYbYtLIgrDE",null);
		setContentView(R.layout.activity_main);
		   if (savedInstanceState == null) {
	            getSupportFragmentManager().beginTransaction()
	                    .add(R.id.container, new PlaceholderFragment())
	                    .commit();
	        }
		   Intent intent_service=new Intent(this, Locate_Data.class);
		   startService(intent_service);//�������� service
		 //  Toast.makeText(this, "��������", 1).show();
		mMapView = (MapView) findViewById(R.id.bmapView);
		mBaiduMap = mMapView.getMap();
		mBaiduMap.setMyLocationEnabled(true);
		preferences=getSharedPreferences("com.example.location_preferences",MODE_PRIVATE);
		isStateLiteOn=preferences.getBoolean("statelite", false);
		String mapZoomBy=preferences.getString("mapzoomPref", "8");
	//	Toast.makeText(this, "���ص����ż���Ϊ"+mapZoomBy,1).show();;
		if(isStateLiteOn){//�������ǵ�ͼ
			mBaiduMap.setMapType(BaiduMap.MAP_TYPE_SATELLITE);
		}else{
			mBaiduMap.setMapType(BaiduMap.MAP_TYPE_NORMAL);
		}
		//���õ�ͼ���ż���,zע�����ͼ��ת��
		mBaiduMap.setMapStatus(MapStatusUpdateFactory.zoomTo(Float.parseFloat(mapZoomBy)));
		mLocationClient = new LocationClient(getApplicationContext());
		// mLocationClient.registerLocationListener(myListener);
		
	}

	public void Locate(View v) {
		LocationClientOption localLocationClientOption = new LocationClientOption();
		localLocationClientOption
				.setLocationMode(LocationClientOption.LocationMode.Hight_Accuracy);
		localLocationClientOption.setCoorType("bd09ll");
		localLocationClientOption.setScanSpan(1000 * 60 * 30);
		localLocationClientOption.setIsNeedAddress(true);
		
		localLocationClientOption.setNeedDeviceDirect(true);
		currentMode = MyLocationConfiguration.LocationMode.NORMAL;
		mCurrentMarker = BitmapDescriptorFactory
				.fromResource(R.drawable.icon_geo);
		mLocationClient.registerLocationListener(myListener);
		mLocationClient.setLocOption(localLocationClientOption);
		mLocationClient.start();
		if ((mLocationClient != null) && (mLocationClient.isStarted())) {
			mLocationClient.requestLocation();
			while (isFirstPoi) {
				isFirstPoi = false;
			//	Log.i("��ͼ״̬��Ϣ--->", mBaiduMap.getMapStatus().toString());
				return;
			}
		}
		
	}

	public class MyLocationListener implements BDLocationListener {

		@Override
		public void onReceiveLocation(BDLocation locationInfo) {
			// TODO Auto-generated method stub
			if ((locationInfo == null || mMapView == null))
				return;
			MyLocationData myLocationData = new MyLocationData.Builder()
					.accuracy(locationInfo.getRadius())
					.latitude(locationInfo.getLatitude())
					.longitude(locationInfo.getLongitude()).build();
			mBaiduMap.setMyLocationData(myLocationData);
			if (isFirstPoi) {
				isFirstPoi = false;
				MapStatusUpdate localMapStatues = MapStatusUpdateFactory
						.newLatLng(new LatLng(locationInfo.getLatitude(),
								locationInfo.getLongitude()));
				mBaiduMap.animateMapStatus(localMapStatues);

			}
			sb = new StringBuffer(256);
			sb.append("��λʱ�䣨time��:");
			sb.append(locationInfo.getTime());
			sb.append(locationInfo.getLocType());
			sb.append("\nγ�� ��latitude��: ");
			sb.append(locationInfo.getLatitude());
			sb.append("\n���ȣ�longitude�� : ");
			sb.append(locationInfo.getLongitude());
			sb.append("\n��λ���ȣ�radius�� : ");
			sb.append(locationInfo.getRadius());
			if (locationInfo.getLocType() == 61) {
				sb.append("\nspeed : ");
				sb.append(locationInfo.getSpeed());
				sb.append("\nsatellite : ");
				sb.append(locationInfo.getSatelliteNumber());
			}
			/*��ȡ��ǰ��γ�Ⱥ͵�ǰ����λ��
			 * 
			 * */
			LOCATION_INFOMATION=sb.toString();
			LOCATE_LATITITUDE=locationInfo.getLatitude();
			LOCATE_LONGTITUDE=locationInfo.getLongitude();
			LOCATITON_NOW=locationInfo.getAddrStr();
			Log.i("--------", String.valueOf(LOCATE_LATITITUDE)+String.valueOf(LOCATE_LONGTITUDE)+LOCATITON_NOW);
			Toast.makeText(getBaseContext(), sb.toString(), 1).show();
			while (isFirstPoi) {
				//�˴������⣬��Ҫ�޸ģ�--->�����Ʋ���ѭ����������
				isFirstPoi = false;
				//Toast.makeText(getBaseContext(), sb.toString(), 1).show();
				
			}

		}

	

	}
	public void Send(View v){
	//	getSIM();
		
		preferences=getSharedPreferences("com.example.location_preferences",MODE_PRIVATE);
		String NUMBER_TO=preferences.getString("editNumPref", "13488463145");
		PendingIntent paIntent = PendingIntent.getBroadcast(this, 0, new Intent(), 0);
		SmsManager smsManager = SmsManager.getDefault();
		smsManager.sendTextMessage(NUMBER_TO, null, LOCATION_INFOMATION, paIntent,null);
		
	}
	public void RouteGuide(View v){
		/*
		 *���е������ڵ���֮ǰ���Ȼ�ȡ��ǰ����λ�ü�������ȶ�λ
		 *��һ��������service�н��ж�λ
		 * */
		/*�˴�����з����봦��������λ��ת��Ϊ��γ������
		 * 
		 * */
		GeoCoder mSearch = null;
		mSearch=GeoCoder.newInstance();
		preferences=getSharedPreferences("com.example.location_preferences",MODE_PRIVATE);
		String Destination=preferences.getString("ditCityPref", "����");
		String destinationDetail=preferences.getString("editDesPref", "������");
		mSearch.geocode(new GeoCodeOption().city(Destination).address(destinationDetail));
		mSearch.setOnGetGeoCodeResultListener(this);
		BaiduNaviManager.getInstance().launchNavigator(this,   
	          LOCATE_LATITITUDE, LOCATE_LONGTITUDE,LOCATITON_NOW,   
	          DESTINATION_LATITUDE, DESTINATION_LONGTITUDE,"Ŀ�ĵ�",  
	            NE_RoutePlan_Mode.ROUTE_PLAN_MOD_MIN_TIME,       //��·��ʽ  
	            true,                                            //��ʵ����  
	            BaiduNaviManager.STRATEGY_FORCE_ONLINE_PRIORITY, //�����߲���  
	            new OnStartNavigationListener() {                //��ת����  
	 
	                @Override  
	                public void onJumpToNavigator(Bundle configParams) {  
	                    Intent intent = new Intent(MainActivity.this, BNavigatorActivity.class);  
	                    intent.putExtras(configParams);  
	                    startActivity(intent);  
	                }  
	 
	                @Override  
	                public void onJumpToDownloader() {  
	                }  
	            });
		
	}
 @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.main, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();
        if (id == R.id.action_settings) {
           // Toast.makeText(getBaseContext(), "��������", 1).show();
            startActivityForResult(new Intent(this, ApprefenceActivity.class), 0);
         if(id==R.id.action_exit){
           	 System.exit(1);
            }
            return true;
        
        }
        return super.onOptionsItemSelected(item);
    }

    /**
     * A placeholder fragment containing a simple view.
     */
    public static class PlaceholderFragment extends Fragment {

        public PlaceholderFragment() {
        }

        @Override
        public View onCreateView(LayoutInflater inflater, ViewGroup container,
                Bundle savedInstanceState) {
            View rootView = inflater.inflate(R.layout.fragment_main, container, false);
            return rootView;
        }
        
    }
	@Override
	public void onGetGeoCodeResult(GeoCodeResult result) {
		// TODO Auto-generated method stub
		if (result == null || result.error != SearchResult.ERRORNO.NO_ERROR) {
			Toast.makeText(this, "��Ǹ��δ���ҵ����", Toast.LENGTH_LONG)
					.show();
			return;
		}
		String strInfo = String.format("γ�ȣ�%f ���ȣ�%f",
				result.getLocation().latitude, result.getLocation().longitude);
		DESTINATION_LATITUDE=result.getLocation().latitude;
		DESTINATION_LONGTITUDE=result.getLocation().longitude;
		//Toast.makeText(this, strInfo, Toast.LENGTH_LONG).show();
	}
	@Override
	public void onGetReverseGeoCodeResult(ReverseGeoCodeResult arg0) {
		// TODO Auto-generated method stub
		
	}
    
	
}
