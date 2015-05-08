package com.example.location;

import com.baidu.navisdk.BaiduNaviManager;
import com.baidu.navisdk.comapi.base.BNSubject;
import com.baidu.navisdk.comapi.mapcontrol.BNMapController;
import com.baidu.navisdk.comapi.routeguide.BNRouteGuider;
import com.baidu.navisdk.comapi.routeplan.BNRoutePlaner;
import com.baidu.navisdk.comapi.tts.BNTTSPlayer;
import com.baidu.navisdk.comapi.tts.BNavigatorTTSPlayer;
import com.baidu.navisdk.comapi.tts.IBNTTSPlayerListener;
import com.baidu.navisdk.model.datastruct.LocData;
import com.baidu.navisdk.model.datastruct.SensorData;
import com.baidu.navisdk.ui.routeguide.BNavigator;
import com.baidu.navisdk.ui.routeguide.IBNavigatorListener;
import com.baidu.navisdk.ui.widget.RoutePlanObserver;
import com.baidu.navisdk.ui.widget.RoutePlanObserver.IJumpToDownloadListener;
import com.baidu.nplatform.comapi.map.MapGLSurfaceView;

import android.app.Activity;
import android.os.Bundle;
import android.view.View;

public class BNavigatorActivity extends Activity {
	private IBNavigatorListener mBNavigatorListener=new IBNavigatorListener() {
		
		@Override
		public void onYawingRequestSuccess() {
			// TODO Auto-generated method stub
			
		}
		
		@Override
		public void onYawingRequestStart() {
			// TODO Auto-generated method stub
			
		}
		
		@Override
		public void onPageJump(int jumpTiming, Object arg) {
			// TODO Auto-generated method stub
			if(IBNavigatorListener.PAGE_JUMP_WHEN_GUIDE_END==jumpTiming){
				finish();
			}else if(IBNavigatorListener.PAGE_JUMP_WHEN_ROUTE_PLAN_FAIL==jumpTiming){
				finish();
			}
		}
		
		@Override
		public void notifyViewModeChanged(int arg0) {
			// TODO Auto-generated method stub
			
		}
		
		@Override
		public void notifyStartNav() {
			// TODO Auto-generated method stub
			
		}
		
		@Override
		public void notifySensorData(SensorData arg0) {
			// TODO Auto-generated method stub
			
		}
		
		@Override
		public void notifyNmeaData(String arg0) {
			// TODO Auto-generated method stub
			
		}
		
		@Override
		public void notifyLoacteData(LocData arg0) {
			// TODO Auto-generated method stub
			
		}
		
		@Override
		public void notifyGPSStatusData(int arg0) {
			// TODO Auto-generated method stub
			
		}
	};

	@Override
	protected void onCreate(Bundle savedInstanceState) {
		// TODO Auto-generated method stub
		super.onCreate(savedInstanceState);
		MapGLSurfaceView mMapView=BaiduNaviManager.getInstance().createNMapView(getApplicationContext());
		View navigatorView=BNavigator.getInstance().init(BNavigatorActivity.this, getIntent().getExtras(), mMapView);
		setContentView(navigatorView);
		BNavigator.getInstance().setListener(mBNavigatorListener);
		BNavigator.getInstance().startNav();
		BNavigatorTTSPlayer.setTTSPlayerListener(new IBNTTSPlayerListener() {
			
			@Override
			public int playTTSText(String arg0, int arg1) {
				// TODO Auto-generated method stub
				return BNTTSPlayer.playTTSText(arg0, arg1);
			}
			
			@Override
			public void phoneHangUp() {
				// TODO Auto-generated method stub
				
			}
			
			@Override
			public void phoneCalling() {
				// TODO Auto-generated method stub
				
			}
			
			@Override
			public int getTTSState() {
				// TODO Auto-generated method stub
				return 0;
			}
		});
		BNRoutePlaner.getInstance().setObserver(new RoutePlanObserver(this,new IJumpToDownloadListener(){

			@Override
			public void onJumpToDownloadOfflineData() {
				// TODO Auto-generated method stub
				
			}}));
	}
	public void onDestroy() {
		BNavigator.destory();
		BNRoutePlaner.getInstance().setObserver(null);
		super.onDestroy();
	}

	public void onPause() {
		BNavigator.getInstance().pause();
		super.onPause();
		BNMapController.getInstance().onPause();
	}

	public void onResume() {
		BNavigator.getInstance().resume();
		super.onResume();
		BNMapController.getInstance().onResume();
	}
	
}
